from flask.cli import FlaskGroup

from SpotifyAuthenticator import application as app

cli = FlaskGroup(app)


if __name__ == "__main__":
    cli()

