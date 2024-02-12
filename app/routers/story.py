from flask import Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schema.schema import EmailSentSchema, FavoriteVideoMailSchema
from app.services.story import StoryService
from app.utils.utils import BASE_URL

storyRouter: Blueprint = Blueprint('StoryController', __name__, url_prefix="/stories")

@storyRouter.post("/")
@cross_origin()
@jwt_required()
def createStory():
    return StoryService.createStory(get_jwt_identity(), request.json)

@storyRouter.get("/<userId>")
@cross_origin()
@jwt_required()
def geStories(userId):
    return StoryService.getStories(userId, get_jwt_identity())


@storyRouter.get("/<userId>/favorite")
@cross_origin()
@jwt_required()
def getFavoriteStories(userId):
    return StoryService.getFavoriteStories(userId, get_jwt_identity())


@storyRouter.get("/friends")
@cross_origin()
@jwt_required()
def getFriendStory():
    return StoryService.getFriendStory(get_jwt_identity())


@storyRouter.get("/")
@cross_origin()
@jwt_required()
def geStory():
    return StoryService.getStory(get_jwt_identity())