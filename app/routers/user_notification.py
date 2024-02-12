from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schema.schema import EmailSentSchema, FavoriteVideoMailSchema
from app.services.story import StoryService
from app.services.user_notification import UserNotificationService
from app.utils.utils import BASE_URL

userNotificationRouter: Blueprint = Blueprint('NotificationController', __name__, url_prefix="/notifications")

@userNotificationRouter.get("/user/<userId>")
@cross_origin()
def getNotifications(userId):
    return UserNotificationService.getNotifications(userId)


@userNotificationRouter.post("/read")
@cross_origin()
@jwt_required()
def markAsRead():
    return UserNotificationService.markAsRead(get_jwt_identity(), request.json)