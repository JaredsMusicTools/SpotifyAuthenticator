#!/usr/bin/env python3.8

# https://stackoverflow.com/questions/40460846/using-flask-inside-class

from FlaskAppWrapper import *
from flask_oauthlib.client import OAuth, OAuthException

from flask import Flask, redirect, url_for, session, request, render_template, flash, send_from_directory, current_app, make_response

PKG_NAME = "SpotifyAuthenticator"

application = Flask(PKG_NAME)

application.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
application.config['consumer_key'] = "e1f239ec0ee443689d6786fd3f397af1" 
application.config['consumer_secret'] = "cbecd4d200f8482d910cb1db77d6f10c"

oauth = OAuth(application)

scope = ['playlist-modify-public', 'user-library-read', 'user-library-modify', 'user-follow-read', 'user-read-private', 'user-top-read']

SPOTIFY_APP_ID = "e1f239ec0ee443689d6786fd3f397af1"
SPOTIFY_APP_SECRET = "cbecd4d200f8482d910cb1db77d6f10c"

spotify = oauth.remote_app(
  'spotify',
  consumer_key=SPOTIFY_APP_ID,
  consumer_secret=SPOTIFY_APP_SECRET,
  request_token_params={'scope': '{}'.format(' '.join(scope))},
  base_url='https://accounts.spotify.com',
  request_token_url=None,
  access_token_url='/api/token',
  authorize_url='https://accounts.spotify.com/authorize'
)

def index(): return ""

def spotify_authorized():
  print("caught!")
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

  # Kill our application
  if(os.environ.get("SHUTDOWN_AFTER_AUTH") == "YES"):
    request.environ.get('werkzeug.server.shutdown')()
    return redirect("https://google.com")
  session.pop('_flashes', None)
  print("Successfully authenticated: {}".format(os.environ['username']), 'success')
  flash("Successfully authenticated: {}".format(os.environ['username']), 'success')
  return redirect("/")

def login():
  # callback = url_for(
    # 'authorized',
    # next=request.args.get('next') or request.referrer or None,
    # _external=True
  # )
  print("authorizing....")
  return spotify.authorize(callback=spotify_authorized)


a = FlaskAppWrapper('wrap', application)

a.add_endpoint(endpoint='/', endpoint_name="index", handler=index, endpoint_type=['GET', 'POST'])
a.add_endpoint(endpoint='/spot/authenticate', endpoint_name='authenticate', handler=login, endpoint_type=['GET', 'POST'])
a.add_endpoint(endpoint='/spot/authenticate/authorized', endpoint_name='authorized', handler=spotify_authorized, endpoint_type=['GET', 'POST'])

a.run()
