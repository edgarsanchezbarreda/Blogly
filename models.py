"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

default_image_url = 'https://merriam-webster.com/assets/mw/images/article/art-wap-article-main/egg-3442-e1f6463624338504cd021bf23aef8441@1x.jpg'

def connect_db(app):
    db.app = app
    db.init_app(app)


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column (
        db.Integer,
        primary_key = True,
        autoincrement = True
    )

    first_name = db.Column (
        db.Text,
        nullable = False,
        unique = True
    )

    last_name = db.Column (
        db.Text,
        nullable = False,
        unique = True
    )

    image_url = db.Column (
        db.Text,
        nullable = False,
        default = default_image_url
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

