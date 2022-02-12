from flask import (
    Flask,
    redirect,
    url_for,
    session,
    request,
    render_template,
    flash,
    send_from_directory,
    current_app,
    make_response,
)
from flask_oauthlib.client import OAuth, OAuthException

from SpotifyAuthenticator import application

import os
import json
import requests
import werkzeug
import typing
from datetime import datetime, timedelta

######################################################################################

oauth = OAuth(application)

scope = [
    "playlist-modify-public",
    "user-library-read",
    "user-library-modify",
    "user-follow-read",
    "user-read-private",
    "user-top-read",
]

spotify = oauth.remote_app(
    "spotify",
    consumer_key=application.config["consumer_key"],
    consumer_secret=application.config["consumer_secret"],
    request_token_params={"scope": f'{" ".join(scope)}'},
    base_url="https://accounts.spotify.com",
    request_token_url=None,
    access_token_url="/api/token",
    authorize_url="https://accounts.spotify.com/authorize",
)

######################################################################################


@application.route("/", methods=["GET", "POST"])
def index():
    """
    User facing component
    """

    session.pop("_flashes", None)

    user_id = os.environ.get("user_id")
    user_name = os.environ.get("username")
    token = os.environ.get("oauth_token")
    time_expires = datetime.now() + timedelta(hours=1)

    if not user_id or not token:
        flash("Please authenticate yourself", "danger")
    else:
        credentials = {
            "user_id": user_id,
            "username": user_name,
            "oauth_token": token,
            "time_expires": time_expires.strftime("%m/%d/%Y %H:%M:%S"),
        }

        with open(
            "/usr/src/app/credentials.json",
            "w",
            encoding="utf-8",
        ) as file_pointer:
            json.dump(credentials, file_pointer)

        return redirect("/") if not session["has_authenticated"] else render_template("home.html")
    return render_template("home.html")


######################################################

"""
This is where the back end authenticator will go
"""


@application.route("/spot/")
def spot_index() -> werkzeug.wrappers.response.Response:
    """
    Base address of the site
    """

    return redirect(url_for("login"))


@application.route("/spot/authenticate")
def login() -> werkzeug.wrappers.response.Response:
    callback = url_for(
        "spotify_authorized",
        next=request.args.get("next") or request.referrer or None,
        _external=True,
    )
    return spotify.authorize(callback=callback)


@application.route("/spot/authenticate/authorized")
def spotify_authorized() -> typing.Union[
    typing.Text, werkzeug.wrappers.response.Response
]:
    response = spotify.authorized_response()
    if response is None:
        return f'Access denied: reason={request.args["error_reason"]} error={request.args["error_description"]}'
    if isinstance(response, OAuthException):
        return f"Access denied: {response.message}"

    session["oauth_token"] = response["access_token"]

    url = "https://api.spotify.com/v1/me"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f'Bearer {session.get("oauth_token")}',
    }

    req = requests.get(url, headers=headers)
    text_response = json.loads(req.text)

    # Set environment variables so they are accessible outside the scope of this application

    os.environ["user_id"] = text_response.get("id")
    os.environ["username"] = text_response.get("display_name")
    os.environ["oauth_token"] = response["access_token"]

    # Keep the variables alive in the session if you wanted to have it all in one script
    session["user_id"] = text_response.get("id")
    session["username"] = text_response.get("display_name")

    session.pop("_flashes", None)
    flash(f"Successfully authenticated: {os.environ['username']}", "success")

    session["has_authenticated"] = True

    return redirect("/")


@application.route("/shutdown", methods=["GET", "POST"])
def shutdown() -> typing.Text:
    """
    Shutdown the server programatically
    NOTE: this method is soon to be depreicated

    Return:
        typing.Text: Message notifying the shutdown
    """

    if not (function := request.environ.get("werkzeug.server.shutdown")):
        raise RuntimeError("Not running the server and I cannot shutdown")

    function()
    return "Server shutting down...."


@spotify.tokengetter
def get_spotify_oauth_token() -> typing.Text:
    """
    Get the OAuth token of the current browser session

    Return:
        typing.Text: String representation of the OAuth token
    """

    return session["oauth_token"]
