from app.configuration.config import sql
from app.model.entity.tag import Tag
from app.model.repository.repo import Repository
from app.model.entity.storytag import StoryTag

class TagRepository(Repository):

    @classmethod
    def getTags(cls):
        tags = sql.session.query(Tag).order_by(Tag.name).all()
        return tags

    @classmethod
    def getTag(cls, tagId):
        tags = sql.session.query(Tag).filter(Tag.tag_id == tagId).first()
        return tags