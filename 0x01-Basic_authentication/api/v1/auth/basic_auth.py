#!/usr/bin/env python3
""" Basic Auth Class
"""

from flask import request
from api.v1.auth.auth import Auth
import base64


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
            base64.b64decode(bah, validate=True)
        except (base64.binascii.Error, ValueError):
            return None

        return base64_authorization_header.decode('utf-8')
