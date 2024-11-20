#!/usr/bin/env python3

"""
Authentication Module
"""

import bcrypt


def _hash_password(self, password: str) -> str:
    """
    Hashes a password using bcrypt.
    pyc"""

    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
