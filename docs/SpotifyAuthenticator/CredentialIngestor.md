# Credentialingestor

> Auto-generated documentation for [SpotifyAuthenticator.CredentialIngestor](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py) module.

- [Spotifyauthenticator](../README.md#spotifyauthenticator) / [Modules](../MODULES.md#spotifyauthenticator-modules) / [Spotifyauthenticator](index.md#spotifyauthenticator) / Credentialingestor
    - [CredentialIngestor](#credentialingestor)
        - [CredentialIngestor().get_credential_hash](#credentialingestorget_credential_hash)
        - [CredentialIngestor().get_map](#credentialingestorget_map)
        - [CredentialIngestor().get_time_expires](#credentialingestorget_time_expires)
        - [CredentialIngestor().get_user_id](#credentialingestorget_user_id)
        - [CredentialIngestor().get_username](#credentialingestorget_username)
        - [CredentialIngestor().is_expired](#credentialingestoris_expired)

## CredentialIngestor

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L9)

```python
class CredentialIngestor():
    def __init__(path: str):
```

### CredentialIngestor().get_credential_hash

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L27)

```python
def get_credential_hash() -> str:
```

### CredentialIngestor().get_map

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L17)

```python
def get_map() -> dict:
```

### CredentialIngestor().get_time_expires

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L30)

```python
def get_time_expires() -> datetime:
```

### CredentialIngestor().get_user_id

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L21)

```python
def get_user_id() -> str:
```

### CredentialIngestor().get_username

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L24)

```python
def get_username() -> str:
```

### CredentialIngestor().is_expired

[[find in source code]](https://github.com/JaredsMusicTools/SpotifyAuthenticator/blob/main/SpotifyAuthenticator/CredentialIngestor.py#L33)

```python
def is_expired(time: datetime) -> bool:
```
