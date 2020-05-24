#!/usr/bin/env python3.8

import json
from datetime import datetime
import os

from SpotifyPlaylist import PlaylistManager

class CredentialIngestor():
    def __init__(self, path: str):
        self.path = path
        self.map = self.get_map()
        self.user_id = self.get_user_id()
        self.credential_hash = self.get_credential_hash()
        self.expire_time = self.get_time_expires()

    def get_map(self) -> dict:
        with open(self.path, "r") as fp:
            return json.load(fp)

    def get_user_id(self) -> str:
        return self.map['user_id']

    def get_credential_hash(self) -> str:
        return self.map['oauth_token']

    def get_time_expires(self) -> datetime:
        return datetime.strptime(self.map['time_expires'], "%m/%d/%Y %H:%M:%S")

    def is_expired(self, time: datetime) -> bool:
        return self.expire_time < time

def generate_manager(credential_path: str):
  if(os.path.exists(credential_path)):
    credential_manager = CredentialIngestor(credential_path)
    if(credential_manager.is_expired(datetime.now())):
      application.run()
  else:
    application.run()
    credential_manager = CredentialIngestor(credential_path)

  return PlaylistManager(
      credential_manager.user_id,
      credential_manager.credential_hash
  )
