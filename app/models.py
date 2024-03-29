from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import Login_manager
from sqlalchemy import func
from datetime import datetime


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    password_hash = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())

    blog = db.relationship('Blog', backref='user', lazy='dynamic')
    comment = db.relationship('Comment', backref='user', lazy="dynamic")

    @property
    def password(self):
        raise AttributeError('password cannot be read')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'User {self.firstname}'


class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    text = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    category = db.Column(db.String(255))
    posted_at = db.Column(db.DateTime, index=True, default=func.now())
    comment = db.relationship('Comment', backref='blogs', lazy='dynamic')

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    def get_blogss(self):
        blogs = Blog.query.all()
        return posts

    def get_blog(self):
        blog = Blog.query.filter_by(id)
        return blog

    def delete_blog(self):
        db.session.clear(self)
        db.session.commit()


class Comment(db.Model):

    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    post_id = db.Column(db.Integer, db.ForeignKey('blogs.id'))
    post_comment = db.Column(db.Text)
    posted = db.Column(db.DateTime, default=datetime.utcnow)

    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    def delete_comment(self):
        db.session.clear(self)
        db.session.commit()


@Login_manager.user_loader
def load_user(username):
    return User.query.get(int(username))


class Quote:

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote


class Subscribers(db.Model):

    __tablename__ = 'subs'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.Text)
