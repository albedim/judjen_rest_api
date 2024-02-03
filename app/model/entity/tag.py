import datetime
import enum

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL, getPlaceDetails


class Tag(sql.Model):
    __tablename__ = "tags"
    tag_id = sql.Column(sql.Integer, primary_key=True)
    name = sql.Column(sql.String(14))

    def __init__(self, name):
        self.name = name

    def toJSON(self, **kvargs):
        obj = {
            'tag_id': self.tag_id,
            'name': self.name
        }
        for kvarg in kvargs:
            obj[kvarg] = kvargs[kvarg]
        return obj