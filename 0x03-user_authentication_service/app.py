#!/usr/bin/env python3

"""
Basic Flask App
"""

from user import User
from auth import Auth
from flask import Flask, jsonify, request, abort, redirect

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'])
def welcome():
    """
    root route returning a welcome
    message.
    """

    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'])
def users():
    """
    Register a new user endpoint
    """

    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    try:
        user = AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    """
    Login endpoint
    """

    email = request.form.get('email')
    password = request.form.get('password')

    if not AUTH.valid_login(email, password):
        abort(401)

    session_id = AUTH.create_session(email)
    response = jsonify({
        "email": email,
        "message": "logged in"
    })

    response.set_cookie('session_id', session_id)

    return response


@app.route('/sessions', methods=['DELETE'], strict_slashes=False)
def logout():
    """
    Logout endpoint.
    """

    session_id = request.cookies.get('session_id')

    user = AUTH.get_user_from_session_id(session_id)

    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    abort(403)


@app.route('/profile', methods=['GET'], strict_slashes=False)
def profile():
    """
    Profile
    """

    session_id = request.cookies.get('session_id')

    if not session_id:
        return jsonify({'error', 'Unauthorized'}), 403

    if user:
        user = AUTH.get_user_from_session_id(session_id)
        return jsonify({'email', user.email}), 200
    abort(403)


if __name__ == "__main__":
    app.run(host='0.0.0', port='5000')
