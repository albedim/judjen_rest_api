from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema
from app.services.friend import FriendService
from app.services.friendrequest import FriendRequestService

friendRouter: Blueprint = Blueprint('FriendController', __name__, url_prefix="/friends")


@friendRouter.post("/reject")
@cross_origin()
@jwt_required()
def rejectRequest():
    return FriendRequestService.reject(get_jwt_identity(), request.json)


@friendRouter.delete("/<friendId>")
@cross_origin()
@jwt_required()
def removeFriend(friendId):
    return FriendService.remove(get_jwt_identity(), friendId)


@friendRouter.post("/accept")
@cross_origin()
@jwt_required()
def acceptRequest():
    return FriendRequestService.accept(get_jwt_identity(), request.json)


@friendRouter.get("/")
@cross_origin()
@jwt_required()
def getFriends():
    return FriendService.getFriends(get_jwt_identity())


@friendRouter.get("/sent")
@cross_origin()
@jwt_required()
def getSentFriendRequests():
    return FriendRequestService.getSentFriendRequests(get_jwt_identity())


@friendRouter.get("/received")
@cross_origin()
@jwt_required()
def getReceivedFriendRequests():
    return FriendRequestService.getReceivedFriendRequests(get_jwt_identity())


@friendRouter.post("/")
@cross_origin()
@jwt_required()
def createRequest():
    return FriendRequestService.create(get_jwt_identity(), request.json)