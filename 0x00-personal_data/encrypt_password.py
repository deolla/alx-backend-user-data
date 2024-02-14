#!/usr/bin/env python3
""" Implement a hash_password function."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This validate the password"""
    validate = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        validate = True
    return validate
