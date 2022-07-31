from flask import request, jsonify, make_response
from flask.globals import current_app
from app import db
from app.models import User
from app.auth import bp
from app.auth.utils import generate_response
from sqlalchemy.exc import IntegrityError


@bp.route('/register', methods=['POST'])
def register():
    data = request.form
    user = User(username=data['username'], email=data['email'])
    user.set_password(data['password'])
    db.session.add(user)
    try:
        db.session.commit()
    except IntegrityError:
        return jsonify(message="User with that email already exists"), 409
    return generate_response(user, "User Created Successfully")


@bp.route('/login', methods=['POST'])
def login():
    form = request.form
    print(form["password"])
    user = User.query.filter(User.lowercase_username == form['username'].lower()).first()
    if user is None or not user.check_password(form['password']):
        return jsonify(message="Incorrect Username or password"), 401
    return generate_response(user, "Login Successful")


@bp.route('/logout', methods=['GET'])
def logout():
    resp = make_response("Success")
    resp.set_cookie(key=current_app.config['REMEMBER_COOKIE_NAME'], value='', expires=0)
    return resp


@bp.route('/refresh_token', methods=['POST'])
def get_session_token():
    print(1)


@bp.route('/refresh_session', methods=['POST'])
def refresh_remember_me():
    print(1)
