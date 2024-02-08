#!/usr/bin/env python3
""" Implement a hash_password function."""
import bcrypt


def hash_password(password: str) -> bytes:
    """Returns a salted, hashed password, which is a byte string."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hash_password: bytes, password: str) -> bool:
    """Returns a boolean."""
    return bcrypt.checkpw(password.encode("utf-8"), hash_password)
