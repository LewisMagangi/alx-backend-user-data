#!/usr/bin/env python3
"""
Password Encryption and Validation Module
"""

import bcrypt

def hash_password(password: str) -> bytes:
    """
    Generate a hashed version of the password with a salt.
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Verify if a provided password matches the hashed password.
    """
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
