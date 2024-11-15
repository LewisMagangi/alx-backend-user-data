#!/usr/bin/env python3
""" Session Authentication
"""
from typing import TypeVar
from api.v1.auth.auth import Auth
from flask import request
from uuid import uuid4
from os import getenv
from models.user import User


class SessionAuth(Auth):
    """
    A session Authentication Class.
    """

    user_id_by_session_id = {}
    """
    A dictionary to store user_id by session_id
    """

    def __init__(self):
        """ Initialisation code block
        """

    def create_session(self, user_id: str = None) -> str:
        """
        Creates a new session for a user
        """

        if user_id is None or type(user_id) is not str:
            return None

        session_id = str(uuid4())
        self.user_id_by_session_id[session_id] = user_id

        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """
        pass
        """

        if session_id is None or not isinstance(session_id, str):
            return None

        return self.user_id_by_session_id.get(session_id)

    def current_user(self, request=None):
        """
        A method that returns a
        User instance based on a cookie value:
        """

        if request is None:
            return None

        session_id = self.session_cookie(request)

        if session_id is None:
            return None

        user_id = self.user_id_for_session_id(session_id)

        if user_id is None:
            return None

        try:
            return User.get(user_id)
        except Exception:
            return None
