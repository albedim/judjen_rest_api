from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.repost import Repost
from app.model.repository.repo import Repository

class RepostRepository(Repository):

    ...

    @classmethod
    def getRepost(cls, user_id, story_id):
        repost = sql.session.query(Repost).filter(Repost.user_id == user_id).filter(Repost.story_id == story_id).first()
        return repost

    @classmethod
    def create(cls, user_id, story_id):
        repost = Repost(user_id, story_id)
        sql.session.add(repost)
        sql.session.commit()
        return repost

    @classmethod
    def remove(cls, user_id, story_id):
        repost = sql.session.query(Repost).filter(Repost.user_id == user_id).filter(Repost.story_id == story_id).delete()
        sql.session.commit()