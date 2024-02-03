from flask import Flask, Blueprint, request

from app.schema.schema import UserCompleteSchema, ContactCreateSchema
from app.services.storytag import StoryTagService

storytagRouter: Blueprint = Blueprint('StoryTagController', __name__, url_prefix="/storytags")

