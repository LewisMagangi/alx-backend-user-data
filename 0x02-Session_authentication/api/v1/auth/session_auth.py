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

    pass
    def create_session(self, user_id: str = None) -> str:
        if user_id is None or type(user_id) is not str:
            return None
        id = uuid4()
        self.user_id_by_session_id[id] = user_id
        return user_id