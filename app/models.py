from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import Login_manager
from sqlalchemy import func
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'kawi'
    id = db.Column(db.Integer,primary_key = True)
    firstname = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.string(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    blogs = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment',backref = 'user', lazy = "dynamic")

    @property
    def password(self):
        raise AttributeError('password cannot be read')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.firstname}'
        