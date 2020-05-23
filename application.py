#!/usr/bin/env python3.8

from SpotifyAuthenticator import application, CredentialIngestor
from datetime import datetime
import threading

if __name__ == '__main__':

  thread = threading.Thread(target=application.run)
  thread.start()
  while(thread.is_alive()):
    thread.join()

  # run other code here
