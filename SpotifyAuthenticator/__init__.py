from flask import Flask
import os

PKG_NAME = "SpotifyAuthenticator"

application = Flask(PKG_NAME)
application.config['SECRET_KEY'] = os.environ.get('SPOTIFY_SECRET_KEY')
application.config['consumer_key'] = os.environ.get('SPOTIFY_AUTHENTICATOR_CLIENT_ID')
application.config['consumer_secret'] = os.environ.get('SPOTIFY_AUTHENTICATOR_CLIENT_SECRET')

from SpotifyAuthenticator import routes
