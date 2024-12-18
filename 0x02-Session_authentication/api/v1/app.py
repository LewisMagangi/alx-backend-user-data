#!/usr/bin/env python3
"""
Route module for the API
"""
from os import getenv
from api.v1.views import app_views
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from api.v1.auth.basic_auth import BasicAuth


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
auth = None
auth = Auth()

if getenv('AUTH_TYPE') == "basic_auth":
    auth = BasicAuth()

elif getenv('AUTH_TYPE') == "session_auth":
    auth = SessionAuth()


@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    """ Custom handler for 401 Unauthorized errors.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    """ Custom handler for 403 Forbidden errors.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.before_request
def before_request() -> str:
    ''' A decorator to request validation before certain procedures
    '''
    if not auth:
        return

    paths = ['/api/v1/status/', '/api/v1/unauthorized/',
             '/api/v1/forbidden/', '/api/v1/auth_session/login/']

    r = request

    if not auth.require_auth(request.path, paths):
        return

    if not auth.authorization_header(r) and not auth.session_cookie(r):
        abort(401)

    current_user = auth.current_user(request)

    if auth.current_user(request) is None:
        abort(403)

    request.current_user = current_user


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
