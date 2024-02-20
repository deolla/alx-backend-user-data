#!/usr/bin/env python3
""" Auth Module. """
from db import DB
from user import User
import bcrypt
from typing import TypeVar
import uuid


def _hash_password(password: str) -> str:
    """Hash password"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def _generate_uuid() -> str:
    """Generate UUID"""
    return str(uuid.uuid4())
