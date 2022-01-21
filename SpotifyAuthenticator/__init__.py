from flask import Flask
import json
import os

PKG_NAME = "SpotifyAuthenticator"

application = Flask(PKG_NAME)

configuration_path = (
    "/usr/src/app/configuration.json"
)

if not os.path.exists(configuration_path):
    raise ValueError(f"[ERROR] Cannot find configuration at {configuration_path}")

with open(configuration_path, "r") as fp:
    content = json.load(fp)

client_secret, client_id = content["client_secret"], content["client_id"]

application.config["SECRET_KEY"] = "84c1c81be6f347629bf01b97fbbe883c"
application.config["consumer_key"] = client_id
application.config["consumer_secret"] = client_secret

from SpotifyAuthenticator import routes
