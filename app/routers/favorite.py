from flask import Flask, Blueprint, request
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt_identity

from app.schema.schema import UserCompleteSchema, ContactCreateSchema
from app.services.favorite import FavoriteService

favoriteRouter: Blueprint = Blueprint('FavoriteController', __name__, url_prefix="/favorites")

@favoriteRouter.post("/")
@jwt_required()
@cross_origin()
def create():
    return FavoriteService.create(get_jwt_identity(), request.json)

