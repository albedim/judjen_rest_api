from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.repost import Repost
from app.model.entity.user import User
from app.model.entity.user_notification import UserNotification
from app.model.repository.repo import Repository

class UserNotificationRepository(Repository):

    @classmethod
    def create(cls, user_id, targetId, notificationType):
        notification = UserNotification(user_id, targetId, notificationType)
        sql.session.add(notification)
        sql.session.commit()
        return notification

    @classmethod
    def getNotifications(cls, user_id):
        notifications = sql.session.query(UserNotification, User).join(User, User.user_id == UserNotification.target_id).filter(UserNotification.user_id == user_id).all()
        return notifications

    @classmethod
    def getNotification(cls, notificationId):
        notification = sql.session.query(UserNotification).filter(UserNotification.notification_id == notificationId).first()
        return notification

    @classmethod
    def markAsRead(cls, notificationId):
        notification = sql.session.query(UserNotification).filter(UserNotification.notification_id == notificationId).delete()
        sql.session.commit()

    @classmethod
    def markAllAsRead(cls, user_id):
        notifications = sql.session.query(UserNotification).filter(UserNotification.user_id == user_id).delete()
        sql.session.commit()