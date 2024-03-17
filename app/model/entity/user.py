import datetime

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL


class User(sql.Model):
    __tablename__ = "users"
    user_id = sql.Column(sql.String(4), primary_key=True)
    email = sql.Column(sql.String(64), nullable=False)
    available_stories = sql.Column(sql.Integer, nullable=False)
    as_limit_date = sql.Column(sql.Date, nullable=True)
    bio = sql.Column(sql.String(80))
    recovery_token = sql.Column(sql.String(16), nullable=True)
    password = sql.Column(sql.String(64), nullable=False)
    anonymous_name = sql.Column(sql.String(24), nullable=False)
    created_on = sql.Column(sql.Date, nullable=False)

    def __init__(self, bio, anonymousName, email, password):
        self.user_id = generateUuid(size=4)
        self.email = email
        self.available_stories = 10
        self.bio = bio
        self.password = password
        self.anonymous_name = anonymousName
        self.created_on = datetime.datetime.utcnow()

    def toJSON(self, **kvargs):
        obj = {
            'user_id': self.user_id,
            'email': self.email,
            'bio': self.bio if self.bio is not None else "Questo sono io in poche parole",
            'anonymous_name': self.anonymous_name,
            'created_on': str(self.created_on)
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj