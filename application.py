#!/usr/bin/env python3.8

def placeholder():
    """
    this some how prevents circular dependencies
    """

    from SpotifyAuthenticator import application as app
    from datetime import datetime
    import threading

    CREDENTIAL_SAVED_PTH = "credentials.json"
    app.run()
placeholder()
