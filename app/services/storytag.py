from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.repository.storytag import StoryTagRepository
from app.model.repository.repo import Repository

class StoryTagService(Repository):

    ...