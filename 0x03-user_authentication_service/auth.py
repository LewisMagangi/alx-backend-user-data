#!/usr/bin/env python3

"""
Authentication Module
"""

from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound


class Auth:
    """
    Auth Class to interact with Authentication Database
    """

    def __init__(self):
        """
        Initialization of the module
        """

        self._db = DB

    def _hash_password(password: str) -> bytes:
        """
        Hashes a password using bcrypt.
        """

        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user in the database.
        """

        try:
            self.db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = self._hash_password(password)
            return self._db.add_user(email, hashed_password)
