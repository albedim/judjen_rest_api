import datetime
import enum

from sqlalchemy import String, Column, Date, Boolean, DateTime
from app.configuration.config import sql
from app.utils.utils import generateUuid, BASE_URL, getPlaceDetails


class UserNotification(sql.Model):
    __tablename__ = "user_notifications"
    notification_id = sql.Column(sql.Integer, primary_key=True)
    user_id = sql.Column(sql.String(4), sql.ForeignKey('users.user_id'), nullable=False)
    target_id = sql.Column(sql.String(4), sql.ForeignKey('users.user_id'), nullable=False)
    notification_type = sql.Column(sql.Integer, nullable=False)
    datetime = sql.Column(sql.DateTime, nullable=False)

    def __init__(self, userId, targetId, notificationType):
        self.user_id = userId
        self.target_id = targetId
        self.datetime = datetime.datetime.utcnow()
        self.read = False
        self.notification_type = notificationType