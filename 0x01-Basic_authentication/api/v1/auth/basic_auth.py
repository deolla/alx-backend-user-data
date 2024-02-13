#!/usr/bin/env python3
""" Basic authentication module, inherits from Auth. """
from api.v1.auth.auth import Auth
from typing import TypeVar
import base64
from models.user import User


class BasicAuth(Auth):
    """Basic authentication module, inherits from Auth.

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        # Extracts base64 authorization header.
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith("Basic "):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
         # Decodes base64 authorization header.
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            return base64.b64decode(base64_authorization_header.encode("utf-8")).decode(
                "utf-8"
            )
        except Exception:
            return None

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        # Extracts user credentials.
        if decoded_base64_authorization_header is None:
            return (None, None)
        if type(decoded_base64_authorization_header) is not str:
            return (None, None)
        if ":" not in decoded_base64_authorization_header:
            return (None, None)
        return tuple(decoded_base64_authorization_header.split(":", 1))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar("User"):
        # User object from credentials.
        if user_email is None or user_pwd is None:
            return None
        if type(user_email) is not str or type(user_pwd) is not str:
            return None
        try:
            user = User.search({"email": user_email})
        except Exception:
            return None
        if user is None:
            return None
        if not user.is_valid_password(user_pwd):
            return None
        return user

    def current_user(self, request=None) -> TypeVar("User"):
        # Current user.
        auth_header = self.authorization_header(request)
        if auth_header is None:
            return None
        encoded_header = self.extract_base64_authorization_header(auth_header)
        if encoded_header is None:
            return None
        decoded_header = self.decode_base64_authorization_header(encoded_header)
        if decoded_header is None:
            return None
        user_credentials = self.extract_user_credentials(decoded_header)
        if user_credentials is None:
            return None
        user = self.user_object_from_credentials(
            user_credentials[0], user_credentials[1]
        )
        return user
    """
