#!/usr/bin/env python3
"""
Views Session Authentication.
"""

from flask import request, jsonify
from api.v1.views import app_views
from models import User
# from api.v1.auth import auth Imported Locally
from os import getenv
from api.v1.app import app


'''
@app.route('/auth_session/login', methods['POST'], strict_slashes=False)
def login():
    """
    Login user with session authentication.
    """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify("{error}:{email missing}"), 400

    if not password:
        return jsonify("{error}:{password missing}"), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify("{error}:{no user found for this email}"), 404

    if not users or len(users) == 0:
        return jsonify("{error}:{no user found for this email}"), 404

    for user in users:
        if user.is_valid_password(password):
            user_id = user.id

            from api.v1.app import auth

            session_id = auth.create_session(user_id)
            response = jsonify(user.to_json())
            response.set.cookie(
                getenv('SESSION_NAME'),
                session_id
                )
            return response
    return jsonify('{error}:{wrong password}'), 401
'''


@app.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    Return:
      - Response
    """
    user_email = request.form.get('email')
    user_pwd = request.form.get('password')
    if not user_email:
        return jsonify(error="email missing"), 400
    if not user_pwd:
        return jsonify(error="password missing"), 400
    try:
        user = User.search({"email": user_email})
    except Exception:
        return jsonify(error="no user found for this email"), 404
    if not user:
        return jsonify(error="no user found for this email"), 404
    for u in user:
        if u.is_valid_password(user_pwd):
            user_id = u.id
            from api.v1.app import auth
            session_id = auth.create_session(user_id)
            response = jsonify(u.to_json())
            response.set_cookie(getenv('SESSION_NAME'), session_id)
            return response
        else:
            return jsonify(error="wrong password"), 401
    return jsonify(error="no user found for this email"), 404
