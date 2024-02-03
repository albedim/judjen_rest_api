from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.favorite import Favorite
from app.model.entity.repost import Repost
from app.model.entity.story import Story
from app.model.entity.user import User
from app.model.repository.repo import Repository


class StoryRepository(Repository):

    @classmethod
    def create(cls, title, userId, content):
        story = Story(userId, title, content)
        sql.session.add(story)
        sql.session.commit()
        return story

    @classmethod
    def getStory(cls, storyId):
        story = sql.session.query(Story).filter(Story.story_id == storyId).first()
        return story

    @classmethod
    def getRandomStory(cls):
        story = sql.session.query(Story, User, text("reposts"), text("favorites")).from_statement(
            text("SELECT stories.*, users.*,"
                 "    (SELECT COUNT(*) "
                 "     FROM reposts "
                 "     WHERE story_id = stories.story_id) AS reposts, "
                 "    (SELECT COUNT(*) "
                 "     FROM favorites "
                 "     WHERE story_id = stories.story_id) AS favorites "
                 "FROM stories "
                 "JOIN users "
                 "ON users.user_id = stories.user_id "
                 "ORDER BY RAND()")
        ).first()
        return story

    @classmethod
    def getStories(cls, userId):
        query = (
            sql.session.query(
                Story,
                User,
                text('reposts'),
                text('favorites')
            ).from_statement(
                text("SELECT stories.*, users.*, "
                     "(SELECT COUNT(*) "
                     "FROM reposts "
                     "WHERE reposts.story_id = stories.story_id) AS reposts, "
                     "(SELECT COUNT(*) FROM favorites WHERE favorites.story_id = stories.story_id) AS favorites "
                     "FROM stories "
                     "LEFT JOIN reposts "
                     "ON reposts.story_id = stories.story_id "
                     "JOIN users ON users.user_id = stories.user_id "
                     "WHERE stories.user_id = :userId OR reposts.user_id = :userId "
                     "ORDER BY reposts.date, stories.created_on DESC").params(userId=userId)
            )
        )

        stories = query.all()
        return stories

    @classmethod
    def getFavoriteStories(cls, userId):
        query = sql.session.query(
            Story,
            User,
            text('reposts'),
            text('favorites')
        ).from_statement(
            text("SELECT stories.*, users.*, "
                "(SELECT COUNT(*) FROM reposts WHERE reposts.story_id = stories.story_id) AS reposts, "
                "(SELECT COUNT(*) FROM favorites WHERE favorites.story_id = stories.story_id) AS favorites "
                "FROM stories "
                "JOIN users ON users.user_id = stories.user_id "
                "JOIN favorites "
                "ON favorites.story_id = stories.story_id "
                "WHERE favorites.user_id = :userId").params(userId=userId)
        )

        stories = query.all()
        return stories