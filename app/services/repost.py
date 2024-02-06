from datetime import datetime

from sqlalchemy import func, text

from app.configuration.config import sql
from app.model.entity.repost import Repost
from app.model.repository.repo import Repository
from app.model.repository.repost import RepostRepository
from app.model.repository.story import StoryRepository
from app.model.repository.user import UserRepository
from app.utils.errors.GException import GException
from app.utils.errors.StoryNotFoundException import StoryNotFoundException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.utils import createSuccessResponse, createErrorResponse


class RepostService(Repository):

    @classmethod
    def create(cls, auth, request):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            story = StoryRepository.getStory(request['story_id'])
            if story is None:
                raise StoryNotFoundException()

            repost = RepostRepository.getRepost(user.user_id, story.story_id)
            if repost is None:
                RepostRepository.create(user.user_id, story.story_id)
            else:
                RepostRepository.remove(user.user_id, story.story_id)
            return createSuccessResponse({'created': repost is None})
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except StoryNotFoundException:
            return createErrorResponse(StoryNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))



