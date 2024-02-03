from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schema.schema import UserAuthSchema, UserRefreshSchema, UserCompleteSchema, UserSigninSchema, TokenData
from app.services.user import UserService

userRouter: Blueprint = Blueprint('UserController', __name__, url_prefix="/users")

@userRouter.post("/signin")
def signin():
    return UserService.signin(request.json)

@userRouter.post("/signup")
def signup():
    return UserService.signup(request.json)

@userRouter.get("/<userId>")
def getUser(userId: str):
    return UserService.getUser(userId)

@userRouter.get("/<userId>/image")
def getUserImage(userId: str):
    return UserService.getUserImage(userId)

@userRouter.get("/query")
@jwt_required()
def getUsers():
    return UserService.getMatchingUsers(get_jwt_identity(), request.args.get("name"))

@userRouter.post("/sync")
@jwt_required()
def sync():
    return UserService.sync(get_jwt_identity())