from flask import Flask, Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import get_jwt_identity, jwt_required

from app.schema.schema import UserCompleteSchema, ContactCreateSchema
from app.services.repost import RepostService

repostRouter: Blueprint = Blueprint('RepostController', __name__, url_prefix="/reposts")

@repostRouter.post("/")
@cross_origin()
@jwt_required()
def create():
    return RepostService.create(get_jwt_identity(), request.json)