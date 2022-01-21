# SpotifyAuthenticator

A Flask application that will authenticate you for Spotify.

## Running

```bash
sudo docker-compose build
sudo docker-compose up -d
```

## Extracting Credentials

```bash
sudo docker cp [CONTAINER_ID]:/usr/src/app/credentials.json .
```
