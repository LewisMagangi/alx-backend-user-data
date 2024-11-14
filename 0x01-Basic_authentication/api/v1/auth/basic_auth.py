#!/usr/bin/env python3
""" Basic Auth Class
"""

from flask import request
from api.v1.auth.auth import Auth
import base64
from typing import TypeVar

User = TypeVar('User')


class BasicAuth(Auth):
    """ A Basic Authentication Class inheriting from Auth Class
    """

    def __init__(self):
        """
        Initialization for BasicAuth (if needed)
        """

        pass

    def extract_base64_authorization_header(self, authorization_header: str):
        """
        Extracts the Base64 part of the Authorization header
        for a Basic Authentication.
        """

        ah = authorization_header
        if ah is None or type(ah) is not str or not ah.startswith("Basic "):
            return None
        return ah.split("Basic ")[1]

    def decode_base64_authorization_header(self, base64_authorization_header):
        """
        Decodes the string from base 64
        """
        bah = base64_authorization_header
        if bah is None or type(bah) is not str:
            return None

        try:
            decoded_bytes = base64.b64decode(bah, validate=True)
        except (base64.binascii.Error, ValueError):
            return None

        return decoded_bytes.decode('utf-8')

    def extract_user_credentials(self, decoded_base64_authorization_header):
        """
        A method that extracts user credentials such as
        email and password and returns them
        """

        dbah = decoded_base64_authorization_header

        if dbah is None or not isinstance(dbah, str) or ":" not in dbah:
            return None, None

        email, password = dbah.split(":")

        return email, password

    def user_object_from_credentials(self, user_email, user_pwd):
        """
        A method in the class BasicAuth that returns:
        the User instance based on his email and password
        """

        e = user_email
        p = user_pwd
        if e is None or type(e) is not str or p is None or type(p) is not str:
            return None

        try:
            user = User.search({"email": e})
        except Exception:
            return None

        if user is None or len(user) == 0:
            return None

        for us in user:
            if us.is_valid_password(p):
                return us

        return None
