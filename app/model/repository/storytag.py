from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.storytag import StoryTag
from app.model.entity.tag import Tag
from app.model.repository.story import Story
from app.model.repository.repo import Repository

class StoryTagRepository(Repository):

    ...
    @classmethod
    def create(cls, storyId, tagId):
        storyTag = StoryTag(tagId, storyId)
        sql.session.add(storyTag)
        sql.session.commit()

    @classmethod
    def getTags(cls, storyId):
        tags = sql.session.query(Tag).join(StoryTag, Tag.tag_id == StoryTag.tag_id).filter(StoryTag.story_id == storyId).all()
        return tags