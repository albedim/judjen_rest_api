from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.favorite import Favorite
from app.model.repository.favorite import FavoriteRepository
from app.model.repository.repo import Repository
from app.model.repository.story import StoryRepository
from app.model.repository.user import UserRepository
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.utils import createSuccessResponse


class FavoriteService(Repository):

    @classmethod
    def create(cls, auth, request):
        userId = auth['user_id']
        user = UserRepository.getUserById(userId)

        if user is None:
            raise UnAuthorizedException()

        story = StoryRepository.getStory(request['story_id'])
        if story is None:
            raise UnAuthorizedException()

        repost = FavoriteRepository.getFavorite(user.user_id, story.story_id)
        if repost is None:
            FavoriteRepository.create(user.user_id, story.story_id)
        else:
            FavoriteRepository.remove(user.user_id, story.story_id)
        return createSuccessResponse({'created': repost is None})