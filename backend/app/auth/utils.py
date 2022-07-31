import json
import jwt

from functools import wraps
from flask import request, current_app, g, make_response, jsonify
from datetime import datetime, timedelta, timezone
from jwt import ExpiredSignatureError


def generate_token(user):
    expiration = datetime.now(tz=timezone.utc) + timedelta(days=365)
    token = jwt.encode({'exp': expiration, 'username': user.username}, current_app.config['SECRET_KEY'], algorithm="HS256")
    return token


def generate_response(user, response):
    token = generate_token(user)
    resp = make_response(jsonify(response), 200)
    resp.set_cookie(key=current_app.config['REMEMBER_COOKIE_NAME'], value=token, secure=True, max_age=timedelta(days=365), httponly=True)
    return resp


def verify_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
    except ExpiredSignatureError:
        return False
    return payload


def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.cookies.get(current_app.config['REMEMBER_COOKIE_NAME'], None) or request.headers.get('Authorization', None)
        if token:
            string_token = token.encode('ascii', 'ignore')
            user = verify_token(string_token)
            if user:
                g.current_user = user
                return f(*args, **kwargs)
        return jsonify(message="Authentication is required to access this resource"), 401
    return decorated
