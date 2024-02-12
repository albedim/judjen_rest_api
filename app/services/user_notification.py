from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.notification import allNotifications
from app.model.entity.repost import Repost
from app.model.repository.repo import Repository
from app.model.repository.repost import RepostRepository
from app.model.repository.story import StoryRepository
from app.model.repository.user import UserRepository
from app.model.repository.user_notification import UserNotificationRepository
from app.utils.errors.GException import GException
from app.utils.errors.StoryNotFoundException import StoryNotFoundException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.utils import createSuccessResponse, createErrorResponse


class UserNotificationService(Repository):

    @classmethod
    def getNotifications(cls, userId):
        try:
            notifications = UserNotificationRepository.getNotifications(userId)
            unreadNotifications = len(UserNotificationRepository.getNotifications(userId))
            res = []
            for notification in notifications:
                notificationContent = cls.getNotification(notification[0].notification_type)
                res.append({
                    'target': notification[1].toJSON(),
                    'notification_id': notification[0].notification_id,
                    'datetime': notification[0].datetime,
                    'content': notificationContent['content'].replace("{anonymous_name}", notification[1].anonymous_name),
                    'href': notificationContent['href'].replace("{user_id}", notification[1].user_id)
                })
            return createSuccessResponse({'unread_notifications': unreadNotifications, 'res': res})
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except StoryNotFoundException:
            return createErrorResponse(StoryNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def markAsRead(cls, auth, request):
        try:
            authUser = UserRepository.getUserById(auth['user_id'])
            if authUser is None:
                raise UnAuthorizedException()
            if 'notification_id' in request:
                notification = UserNotificationRepository.getNotification(request['notification_id'])
                if notification.user_id != authUser.user_id:
                    raise UnAuthorizedException()
                UserNotificationRepository.markAsRead(request['notification_id'])
            else:
                UserNotificationRepository.markAllAsRead(authUser.user_id)
            return cls.getNotifications(authUser.user_id)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except StoryNotFoundException:
            return createErrorResponse(StoryNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getNotification(cls, notificationType):
        for notification in allNotifications:
            if notification["type"] == notificationType:
                return notification
        return None

