#!/usr/bin/env python3
""" Class to manage the API authentication process. """
from flask import request
from typing import List, TypeVar
from os import getenv


class Auth:
    """Class to manage the API authentication process."""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Method to manage the API authentication process."""
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        pat = len(path)
        if pat == 0:
            return True

        slash_path = True if path[pat - 1] == "/" else False

        tmp_path = path
        if not slash_path:
            tmp_path += "/"

        for exc in excluded_paths:
            exect = len(exc)
            if exect == 0:
                continue

            if exc[exect - 1] != "*":
                if tmp_path == exc:
                    return False
            else:
                if exc[:-1] == path[: exect - 1]:
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """Method to manage the API authentication process."""
        if request is None or "Authorization" not in request.headers:
            return None
        return request.headers["Authorization"]

    def current_user(self, request=None) -> TypeVar("User"):
        """Method to manage the API authentication process."""
        return None

    def session_cookie(self, request=None):
        """Method to manage the API authentication process."""
        if request is None:
            return None
        session_name = getenv("SESSION_NAME")
        return request.cookies.get(session_name)
