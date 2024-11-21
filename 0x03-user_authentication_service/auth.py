#!/usr/bin/env python3

"""
Authentication Module
"""

from db import DB
import bcrypt
from user import User
from sqlalchemy.orm.exc import NoResultFound
import uuid


def _generate_uuid() -> str:
    """
    Generate a random UUID.
    """

    return str(uuid.uuid4())


def _hash_password(password: str) -> bytes:
    """
    Hashes a password using bcrypt.
    """

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """
    Auth Class to interact with Authentication Database
    """

    def __init__(self):
        """
        Initialization of the module
        """

        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        Registers a new user in the database.
        """

        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            return self._db.add_user(email, hashed_password)

    def valid_login(self, email: str, password: str) -> bool:
        """
        Validates a user's login credentials.
        """

        try:
            user = self._db.find_user_by(email=email)
        except NoResultFound:
            return False
        return bcrypt.checkpw(password.encode('utf-8'), user.hashed_password)

    def create_session(self, email: str) -> str:
        """
        Creates a new session for a user.
        """

        try:
            user = self._db.find_user_by(email=email)

            session_id = _generate_uuid()

            self._db.update_user(user.id, session_id=session_id)

            return session_id
        except NoResultFound:
            return None

    def get_user_from_session_id(self, session_id: str) -> User:
        """
        Retrieves a user from a session ID.
        """

        if not session_id:
            return None

        try:
            user = self._db.find_user_by(session_id=session_id)
        except Exception:
            return None
        return user

    def destroy_session(self, user_id) -> None:
        """
        Destroys the current session.
        """

        self._db.update_user(user_id, session_id=None)
