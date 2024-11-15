#!/usr/bin/env python3
""" Session Authentication
"""
from api.v1.auth.auth import Auth
from flask import request
from uuid import uuid4


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
