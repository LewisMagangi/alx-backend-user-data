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

        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        path = path + '/' if path[-1] != '/' else path
        has_wildcard = any(x.endswith("*") for x in excluded_paths)
        if not has_wildcard:
            return path not in excluded_paths
        for e in excluded_paths:
            if e.endswith("*"):
                if path.startswith(e[:-1]):
                    return False
            if path == e:
                return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the Authorization header from the request.
        """
        if request is None:
            return None
        return request.headers.get("Authorization")

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns the current user based on the request.
        Currently, it returns None.
        """
        return None


class SessionAuth(Auth):
    """
    A session Authentication Class.
    """

    def __init__(self):
        """ Initialisation code block
        """

    if not issubclass(SessionAuth, Auth):
        return False

    pass
