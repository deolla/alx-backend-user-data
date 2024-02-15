#!/usr/bin/env python3
"""A class SessionDBAuth that inherits from SessionExpAuth."""
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession
from datetime import datetime, timedelta
import os


class SessionDBAuth(SessionExpAuth):
    """A class SessionDBAuth that inherits from SessionExpAuth."""

    def create_session(self, user_id: str = None) -> str:
        """Create a Session ID for a user_id"""
        session_id = super().create_session(user_id)
        if session_id:
            user_session = UserSession(user_id=user_id, session_id=session_id)
            user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id: str = None) -> str:
        """Return a User ID based on a Session ID"""
        user_id = super().user_id_for_session_id(session_id)
        if user_id:
            user_session = UserSession.search({"session_id": session_id})
            if not user_session:
                return None
            user_session = user_session[0]
            if self.session_duration <= 0:
                return user_id
            created_at = user_session.created_at
            if not created_at:
                return None
            if (datetime.now() - created_at) > timedelta(seconds=self.session_duration):
                return None
            return user_id
        return None

    def destroy_session(self, request=None) -> bool:
        """Destroy a session."""
        if request:
            session_id = self.session_cookie(request)
            if not session_id:
                return False
            user_id = self.user_id_for_session_id(session_id)
            if not user_id:
                return False
            user_session = UserSession.search({"session_id": session_id})
            if not user_session:
                return False
            user_session = user_session[0]
            user_session.remove()
            return True
        return False
