import os

from flask import g, jsonify
from app import create_app
from app.models import User
from app.auth.utils import requires_auth

config_name = os.getenv('FLASK_ENV')
app = create_app(config_name)


@app.shell_context_processor
def make_shell_context():
    return {'User': User}


@app.route("/")
def hello_world():
    return "<p>Hello!</p>"


@app.route("/username")
@requires_auth
def hello():
    return jsonify(g.current_user)
