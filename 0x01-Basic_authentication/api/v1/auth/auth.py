#!/usr/bin/env python3
""" 3. Auth class
"""

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
    
        Returns:
        - True if path is None
        - True if excluded_paths is None or empty
        - False if path is in excluded_paths (considering slash tolerance)
        """
        
        if path is None or excluded_paths is None or len(path) == 0:
            return True
        
        normalized_path = path.rstrip('/')

        for excluded_path in excluded_paths:
            if normalized_path == excluded_path.rstrip('/'):
                return False

        return True

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