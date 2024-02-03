import datetime
import enum

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL, getPlaceDetails


class Favorite(sql.Model):
    __tablename__ = "favorites"
    user_id = sql.Column(sql.String(4), sql.ForeignKey('users.user_id'), primary_key=True)
    story_id = sql.Column(sql.Integer, sql.ForeignKey('stories.story_id'), primary_key=True)
    date = sql.Column(sql.Date, nullable=False)

    def __init__(self, userId, storyId):
        self.user_id = userId
        self.date = datetime.datetime.utcnow()
        self.story_id = storyId