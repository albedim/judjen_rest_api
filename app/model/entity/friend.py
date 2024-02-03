import datetime
import enum

from sqlalchemy import String, Column, Date, Boolean, Enum, ForeignKey
from app.configuration.config import sql
from app.utils.utils import generateUuid


class Friend(sql.Model):
    __tablename__ = 'friends'
    user_id = sql.Column(sql.String(4), ForeignKey('users.user_id'), primary_key=True)
    friend_id = sql.Column(sql.String(4), ForeignKey('users.user_id'), primary_key=True)
    created_on = sql.Column(sql.Date, nullable=False)

    def __init__(self, userId, friendId):
        self.user_id = userId
        self.created_on = datetime.datetime.utcnow()
        self.friend_id = friendId

    def toJSON(self, **kvargs):
        obj = {
            'user_id': self.user_id,
            'friend_id': self.friend_id,
            'created_on': str(self.created_on)
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj