from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.favorite import Favorite
from app.model.repository.repo import Repository

class FavoriteRepository(Repository):

    @classmethod
    def getFavorite(cls, user_id, story_id):
        repost = sql.session.query(Favorite).filter(Favorite.user_id == user_id).filter(Favorite.story_id == story_id).first()
        return repost

    @classmethod
    def create(cls, user_id, story_id):
        repost = Favorite(user_id, story_id)
        sql.session.add(repost)
        sql.session.commit()
        return repost

    @classmethod
    def remove(cls, user_id, story_id):
        repost = sql.session.query(Favorite).filter(Favorite.user_id == user_id).filter(Favorite.story_id == story_id).delete()
        sql.session.commit()