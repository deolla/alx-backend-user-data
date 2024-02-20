#!/usr/bin/env python3
""" Use the requests module to query your web server."""
import requests

BASE_URL = "http://localhost:5000"
EMAIL = "guillaume@holberton.io"
PASSWD = "b4l0u"
NEW_PASSWD = "t4rt1fl3tt3"


def register_user(email: str, password: str) -> None:
    """Register user."""
    r = requests.post(f"{BASE_URL}/users", data={
        "email": email, "password": password
    })
    print(r.status_code, r.json())


def log_in_wrong_password(email: str, password: str) -> None:
    """Log in with wrong password."""
    r = requests.post(
        f"{BASE_URL}/sessions", data={"email": email, "password": password}
    )
    print(r.status_code, r.json())


def profile_unlogged() -> None:
    """Profile of an unlogged user."""
    r = requests.get(f"{BASE_URL}/profile")
    print(r.status_code, r.json())


def log_in(email: str, password: str) -> str:
    """Log in."""
    r = requests.post(
        f"{BASE_URL}/sessions", data={"email": email, "password": password}
    )
    print(r.status_code, r.json())
    return r.cookies.get("session_id")


def profile_logged(session_id: str) -> None:
    """Profile of a logged user."""
    r = requests.get(f"{BASE_URL}/profile", cookies={"session_id": session_id})
    print(r.status_code, r.json())


def log_out(session_id: str) -> None:
    """Log out."""
    r = requests.delete(f"{BASE_URL}/sessions", cookies={
        "session_id": session_id
    })
    print(r.status_code, r.json())


def reset_password_token(email: str) -> str:
    """Reset password token."""
    r = requests.post(f"{BASE_URL}/reset_password", data={"email": email})
    print(r.status_code, r.json())
    return r.json().get("reset_token")


def update_password(email: str, reset_token: str, new_password: str) -> None:
    """Update password."""
    r = requests.put(
        f"{BASE_URL}/reset_password",
        data={
            "email": email,
            "reset_token": reset_token, "new_password": new_password
        },
    )
    print(r.status_code, r.json())


if __name__ == "__main__":

    register_user(EMAIL, PASSWD)
    log_in_wrong_password(EMAIL, NEW_PASSWD)
    profile_unlogged()
    session_id = log_in(EMAIL, PASSWD)
    profile_logged(session_id)
    log_out(session_id)
    reset_token = reset_password_token(EMAIL)
    update_password(EMAIL, reset_token, NEW_PASSWD)
    log_in(EMAIL, NEW_PASSWD)
