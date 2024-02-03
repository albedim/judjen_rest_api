from flask import Flask, Blueprint, request
from flask_cors import cross_origin

from app.schema.schema import UserCompleteSchema, ContactCreateSchema
from app.services.tag import TagService

tagRouter: Blueprint = Blueprint('TagController', __name__, url_prefix="/tags")

@tagRouter.get("/")
@cross_origin()
def getTags():
    return TagService.getTags()
