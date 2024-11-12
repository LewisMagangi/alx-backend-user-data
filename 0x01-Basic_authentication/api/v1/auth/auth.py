#!/usr/bin/env python3
from flask import request
from typing import TypeVar, List

class Auth:
    """ Authentication Class
    """
    def __init__(self):
        """ Initialisation code block
        """
    
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether authentication is required for a given path.
        Currently, it returns False by default.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.
        Currently, it returns None.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the request.
        Currently, it returns None.
        """
        return None