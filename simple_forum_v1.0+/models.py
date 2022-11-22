from datetime import datetime
from routes import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    prof_pic = db.Column(db.String(60), nullable=False, default='default.png')
    date_created = db.Column(db.DateTime, nullable=False,
                             default=datetime.utcnow)
    description = db.Column(db.String(80), nullable=True, default='')
    role = db.Column(db.String(10), nullable=False, default='member')
    posts = db.relationship('Post', backref='user_post', lazy=True)
    comments = db.relationship('Comment', backref='user_comment', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', " \
               f"'{self.password}', '{self.prof_pic}', " \
               f"'{self.date_created}', '{self.role}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(10), nullable=False, default='unlock')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    comments = db.relationship('Comment', cascade='all, delete',
                               backref='post_comment', lazy=True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}', " \
               f"'{self.content}', '{self.category}', '{self.status}')"


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    time_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return f"Comment('{self.content}', '{self.time_posted}')"
