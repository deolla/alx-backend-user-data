#!/usr/bin/env python3
"""A class SessionExpAuth that inherits from SessionAuth."""
from api.v1.auth.session_auth import SessionAuth
from datetime import datetime, timedelta
import os


class SessionExpAuth(SessionAuth):
    """A class SessionExpAuth that inherits from SessionAuth."""

    def __init__(self):
        """Constructor method"""
        duration = os.getenv("SESSION_DURATION")
        if duration:
            self.session_duration = int(duration)
        else:
            self.session_duration = 0

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        if session_id:
            self.user_id_by_session_id[session_id] = {
                "user_id": user_id,
                "created_at": datetime.now(),
            }
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        if session_id is None:
            return None
        session_dict = super().user_id_for_session_id(session_id)
        if session_dict:
            if self.session_duration <= 0:
                return session_dict.get("user_id")
            created_at = session_dict.get("created_at")
            if not created_at:
                return None
            if (datetime.now() - created_at) > timedelta(seconds=self.session_duration):
                return None
            return session_dict.get("user_id")
        return None
