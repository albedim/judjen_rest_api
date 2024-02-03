from flask import Blueprint

from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema
from app.services.friendrequest import FriendRequestService

friendrequestRouter: Blueprint = Blueprint('FriendRequestController', __name__, url_prefix="/friendrequests")