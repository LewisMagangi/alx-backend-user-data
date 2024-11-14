#!/usr/bin/env python3
""" Basic Auth Class
"""

from flask import request
from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ A Basic Authentication Class inheriting from Auth Class
    """

    def __init__(self):
        """
        Initialization for BasicAuth (if needed)
        """

    """ A method that returns the Base64 part of the Authorization header for a Basic Authentication.
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        if authorization_header is None or type(authorization_header) is not str or not authorization_header.startswith("Basic "):
            return None
        return authorization_header.split("Basic ")[1]
    pass
