# Routes

> Auto-generated documentation for [SpotifyAuthenticator.routes](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py) module.

- [Spotifyauthenticator](../README.md#spotifyauthenticator) / [Modules](../MODULES.md#spotifyauthenticator-modules) / [Spotifyauthenticator](index.md#spotifyauthenticator) / Routes
    - [get_spotify_oauth_token](#get_spotify_oauth_token)
    - [index](#index)
    - [login](#login)
    - [shutdown](#shutdown)
    - [spot_index](#spot_index)
    - [spotify_authorized](#spotify_authorized)

## get_spotify_oauth_token

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py#L136)

```python
@spotify.tokengetter
def get_spotify_oauth_token() -> str:
```

## index

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py#L37)

```python
@application.route('/', methods=['GET', 'POST'])
def index():
```

## login

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py#L78)

```python
@application.route('/spot/authenticate')
def login() -> werkzeug.wrappers.response.Response:
```

## shutdown

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py#L127)

```python
@application.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
```

## spot_index

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py#L68)

```python
@application.route('/spot/')
def spot_index() -> werkzeug.wrappers.response.Response:
```

Base address of the site

## spotify_authorized

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/routes.py#L89)

```python
@application.route('/spot/authenticate/authorized')
def spotify_authorized() -> str:
```
