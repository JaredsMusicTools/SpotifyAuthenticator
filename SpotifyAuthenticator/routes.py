from flask import Flask, redirect, url_for, session, request, render_template, flash, send_from_directory, current_app, make_response
from flask_oauthlib.client import OAuth, OAuthException

from SpotifyAuthenticator import application

import os
import json
import requests
import werkzeug
from datetime import datetime, timedelta
from pprint import pprint as pp

######################################################################################

oauth = OAuth(application)

scope = ['playlist-modify-public', 'user-library-read', 'user-library-modify', 'user-follow-read', 'user-read-private', 'user-top-read']

spotify = oauth.remote_app(
  'spotify',
  consumer_key=application.config['consumer_key'],
  consumer_secret=application.config['consumer_secret'],
  request_token_params={'scope': '{}'.format(' '.join(scope))},
  base_url='https://accounts.spotify.com',
  request_token_url=None,
  access_token_url='/api/token',
  authorize_url='https://accounts.spotify.com/authorize'
)

######################################################################################

"""
This is the front end component
"""


@application.route("/", methods=['GET', 'POST'])

def index():

  session.pop('_flashes', None)

  u_id = os.environ.get("user_id")
  u_name = os.environ.get("username")
  token = os.environ.get("oauth_token")
  time_expires = datetime.now()+timedelta(hours=1)

  if((u_id is None) or (token is None)):
    flash("Please authenticate yourself", 'danger')
  else:
    credentials = {
      "user_id": u_id,
      "username": u_name,
      "oauth_token":  token,
      "time_expires": time_expires.strftime("%m/%d/%Y %H:%M:%S")
    }
    with open("credentials.json", 'w') as fp:
        json.dump(credentials, fp)
    return redirect("/shutdown")
  return render_template('home.html')

######################################################

"""
This is where the back end authenticator will go
"""

@application.route('/spot/')

def spot_index() -> werkzeug.wrappers.response.Response:

  """
  Base address of the site 
  """
  return redirect(url_for('login'))


@application.route('/spot/authenticate')

def login() -> werkzeug.wrappers.response.Response:
  callback = url_for(
    'spotify_authorized',
    next=request.args.get('next') or request.referrer or None,
    _external=True
  )
  return spotify.authorize(callback=callback)


@application.route('/spot/authenticate/authorized')

def spotify_authorized() -> str:
  response = spotify.authorized_response()
  if(response is None):
    return 'Access denied: reason={0} error={1}'.format(
      request.args['error_reason'],
      request.args['error_description']
    )
  if isinstance(response, OAuthException):
    return 'Access denied: {0}'.format(response.message)


  session['oauth_token'] = response['access_token']

  url = "https://api.spotify.com/v1/me"
  headers = {
    'Accept': 'application/json', 
    'Content-Type': 'application/json', 
    'Authorization': 'Bearer {}'.format(session.get('oauth_token'))
  }

  req = requests.get(url, headers=headers)
  text_response = json.loads(req.text)

  # Set environment variables so they are accessible outside the scope of this application 
  os.environ['user_id'] = text_response.get('id')
  os.environ['username'] = text_response.get('display_name')
  os.environ['oauth_token'] = response['access_token']

  # Keep the variables alive in the session if you wanted to have it all in one script
  session['user_id'] = text_response.get('id')
  session['username'] = text_response.get('display_name')

  session.pop('_flashes', None)
  flash("Successfully authenticated: {}".format(os.environ['username']), 'success')
  return redirect("/")

@application.route('/shutdown', methods=['GET','POST'])

def shutdown():
    function = request.environ.get('werkzeug.server.shutdown')
    if(function is None):
        raise RuntimeError("Not running the server!")
    function()
    return "Server shutting down...."

@spotify.tokengetter

def get_spotify_oauth_token() -> str:
  return session.get('oauth_token')
