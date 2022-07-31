from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func
from sqlalchemy.ext.hybrid import hybrid_property


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(128), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def serializable(self):
        return {'id': self.id, 'username': self.username}

    @hybrid_property
    def lowercase_username(self):
        return self.username.lower()

    @lowercase_username.expression
    def lowercase_username(cls):
        return func.lower(cls.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
