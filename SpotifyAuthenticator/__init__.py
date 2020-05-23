from flask import Flask
import os

PKG_NAME = "SpotifyAuthenticator"

application = Flask(PKG_NAME)

try:
  application.config['SECRET_KEY'] = os.environ.get('SPOTIFY_SECRET_KEY')
  application.config['consumer_key'] = os.environ.get('SPOTIFY_AUTHENTICATOR_CLIENT_ID')
  application.config['consumer_secret'] = os.environ.get('SPOTIFY_AUTHENTICATOR_CLIENT_SECRET')
except KeyError as invalid_key:
    raise KeyError("[-] You need to set {} in your shell's configuration file".format(invalid_key))

from SpotifyAuthenticator import routes
