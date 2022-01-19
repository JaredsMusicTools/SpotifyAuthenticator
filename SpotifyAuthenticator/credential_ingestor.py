#!/usr/bin/env python

"""
This module contains an implementation for CredentialIngestor,
which will process credentials provided
"""

import json
import datetime
import typing
import pathlib

class CredentialIngestor():
    """
    Class representation of the credentials file
    that is read in before authenticating the user
    """

    def __init__(self, path: pathlib.Path):
        self.path = path
        self.map = self.get_map()
        self.user_id = self.get_user_id()
        self.credential_hash = self.get_credential_hash()
        self.expire_time = self.get_time_expires()

    def get_map(self) -> typing.Dict[typing.Text, typing.Text]:
        """
        Read in the contents of the credentials file and give back
        a Python dictionary object

        Returns:
            typing.Dict[typing.Text, typing.Text]: Python dictionary representation of the credentials file
        """

        with open(self.path, "r", encoding="utf-8") as file_pointer:
            return json.load(file_pointer)

    def get_user_id(self) -> str:
        """
        Get the current Spotify ID

        Returns:
            str: String representation of the Spotify ID
        """

        return self.map["user_id"]

    def get_username(self) -> str:
        """
        Get the current Spotify username

        Returns:
            str: String representation of the Spotify username
        """

        return self.map["username"]

    def get_credential_hash(self) -> str:
        """
        Get the authentication token

        Returns:
            str: String representation of the authentication token
        """

        return self.map["oauth_token"]

    def get_time_expires(self) -> datetime.datetime:
        """
        Obtain a datetime representation when the token expires

        Returns:
            datetime.datetime: datetime object that can be compared against other criteria
        """

        return datetime.datetime.strptime(self.map["time_expires"], "%m/%d/%Y %H:%M:%S")

    def is_expired(self, time: datetime.datetime) -> bool:
        """
        Check if the current token is still valid

        Returns:
            bool: True if expired, False otherwise
        """

        return self.expire_time < time
