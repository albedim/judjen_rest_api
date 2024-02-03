import datetime
import enum

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL, getPlaceDetails


class StoryTag(sql.Model):
    __tablename__ = "storytags"
    tag_id = sql.Column(sql.Integer, sql.ForeignKey('tags.tag_id'), primary_key=True)
    story_id = sql.Column(sql.Integer, sql.ForeignKey('stories.story_id'), primary_key=True)

    def __init__(self, tagId, storyId):
        self.tag_id = tagId
        self.story_id = storyId

    def toJSON(self, **kvargs):
        obj = {
            'tag_id': self.tag_id,
            'story_id': self.story_id
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj