import datetime
import enum

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL


class Story(sql.Model):
    __tablename__ = "stories"
    story_id = sql.Column(sql.Integer, primary_key=True)
    title = sql.Column(sql.String(64), nullable=False)
    content = sql.Column(sql.Text, nullable=False)
    created_on = sql.Column(sql.Date, nullable=False)
    user_id = sql.Column(sql.String(4), sql.ForeignKey('users.user_id'), nullable=False)

    def __init__(self, userId, title, content):
        self.title = title
        self.user_id = userId
        self.content = content
        self.created_on = datetime.datetime.utcnow()

    def toJSON(self, **kvargs):
        obj = {
            'story_id': self.story_id,
            'title': self.title,
            'content': self.content,
            'created_on': str(self.created_on),
            'user_id': self.user_id
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj