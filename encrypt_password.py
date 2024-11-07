#!/usr/bin/env python3
"""
Password Encryption and Validation
"""

import bcrypt


def generate_hashed_password(plain_password: str) -> bytes:
    """
    Generate a salted hash for the given password
    """
    return bcrypt.hashpw(plain_password.encode('utf-8'), bcrypt.gensalt())


def validate_password(stored_hashed_password: bytes, plain_password: str) -> bool:
    """
    Check if the provided password matches the stored hashed password
    """
    return bcrypt.checkpw(plain_password.encode('utf-8'), stored_hashed_password)
