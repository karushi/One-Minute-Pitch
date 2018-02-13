from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255), unique=True, index=True)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    password_hash = db.Column(db.String(255))

    # relationship between user and line class

    lines = db.relationship('Line', backref='user', lazy='dynamic')

    # relationship between user and comment class
    comments = db.relationship('Comment', backref='user', lazy='dynamic')


    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')


    @password.setter
    def password(self, password):

            self.password_hash = generate_password_hash(password)


    def verify_password(self, password):
            return check_password_hash(self.password_hash, password)


    def __repr__(self):
            return 'Pitch {}'.format(self.username)


class Pitch(db.Model):

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))


# relationship between pitch and line class
    lines = db.relationship('Line', backref='pitch', lazy='dynamic')


def save_pitches(self):
            db.session.add(self)
            db.session.commit()


@classmethod
def get_pitches(cls):
            pitches = Pitch.query.all()
            return pitches


class Line(db.Model):
    '''
    Line class to define the pitches
    '''
    __tablename__ = 'lines'
    id = db.Column(db.Integer, primary_key=True)
    line_content = db.Column(db.String(200))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    # user_id column for linking a line to a specific pitch
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))

    # relationship between line and comment class
    comments = db.relationship('Comment', backref='line', lazy='dynamic')


def save_line(self):
        '''
        Function that saves a new pitch to the lines table
        '''
        db.session.add(self)
        db.session.commit()


@classmethod
def get_lines(cls, pitch_id):
        '''
        Function that queries the Lines Table in the database and returns only information with the specified pitch id
        Args:
            group_id : specific group_id
        Returns:
            lines : all the information for lines with the specific pitch id
        '''
        lines = Line.query.order_by(Line.id.desc()).filter_by(pitch_id=pitch_id).all()

        return lines


class Comment(db.Model):
    '''
    Comment class to define the feedback from users
    '''
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String)

    # line_id column for linking a line to a specific line
    line_id = db.Column(db.Integer, db.ForeignKey("lines.id"))

    # user_id column for linking a line to a specific pitch
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))


def save_comment(self):
        '''
        Function that saves a new comment given as feedback to a pitch
        '''
        db.session.add(self)
        db.session.commit()


@classmethod
def get_comments(cls, line_id):
        '''
        Function that queries the Comments Table in the database and returns only information with the specified line id
        Args:
            line_id : specific line_id
        Returns:
            comments : all the information for comments with the specific line id
        '''
        comments = Comment.query.filter_by(line_id=line_id).all()

        return comments
