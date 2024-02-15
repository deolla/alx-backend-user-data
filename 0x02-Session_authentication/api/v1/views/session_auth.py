#!/usr/bin/env python3
""" Create a new view for Session Authentication """
from flask import jsonify, request, abort
from api.v1.views import app_views
from models.user import User
from api.v1.app import auth
from os import getenv


@app_views.route("/auth_session/login", methods=["POST"], strict_slashes=False)
def auth_session() -> str:
    """POST /auth_session/login
    Return:
      - JSON payload
    """
    email = request.form.get("email")
    password = request.form.get("password")

    if email is None or email == "":
        return jsonify({"error": "email missing"}), 400
    if password is None or password == "":
        return jsonify({"error": "password missing"}), 400

    search_user = User.search({"email": email})
    if not search_user:
        return jsonify({"error": "no user found for this email"}), 404

    for user in search_user:
        if not user.is_valid_password(password):
            return jsonify({"error": "wrong password"}), 401

    session_id = auth.create_session(search_user[0].id)
    response = jsonify(search_user[0].to_json())
    response.set_cookie(getenv("SESSION_NAME"), session_id)

    return response


app_views.route("/auth_session/logout", 
                methods=["DELETE"], strict_slashes=False)
def auth_session_logout() -> str:
    """DELETE /auth_session/logout
    Return:
      - JSON payload
    """
    if auth.destroy_session(request):
        return jsonify({}), 200
    abort(404)
