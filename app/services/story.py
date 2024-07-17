import datetime

from app.configuration.config import sql
from app.model.repository.favorite import FavoriteRepository
from app.model.repository.repost import RepostRepository
from app.model.repository.story import StoryRepository
from app.model.repository.repo import Repository
from app.model.repository.storytag import StoryTagRepository
from app.model.repository.tag import TagRepository
from app.model.repository.user import UserRepository
from app.model.repository.user_notification import UserNotificationRepository
from app.services.repost import RepostService
from app.utils.errors.GException import GException
from app.utils.errors.StoryNotFoundException import StoryNotFoundException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.utils import createSuccessResponse, createErrorResponse


class StoryService(Repository):

    @classmethod
    def getStory(cls, auth):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            story = StoryRepository.getRandomStory()

            if story is None:
                raise StoryNotFoundException()

            reposted = RepostRepository.getRepost(user.user_id, story[0].story_id) is not None
            favorited = FavoriteRepository.getFavorite(user.user_id, story[0].story_id) is not None
            res = []
            topics = StoryTagRepository.getTags(story[0].story_id)
            for topic in topics:
                res.append(topic.toJSON())

            return createSuccessResponse({
                'story': story[0].toJSON(
                    topics=res,
                    reposted=reposted,
                    favorited=favorited,
                    user=story[1].toJSON(),
                    reposts=story[2],
                    favorites=story[3]
                )
            })
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except StoryNotFoundException:
            return createErrorResponse(StoryNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getFriendStory(cls, auth):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            story = StoryRepository.getFriendStory(userId)

            if story is None:
                raise StoryNotFoundException()

            reposted = RepostRepository.getRepost(user.user_id, story[0].story_id) is not None
            favorited = FavoriteRepository.getFavorite(user.user_id, story[0].story_id) is not None
            res = []
            topics = StoryTagRepository.getTags(story[0].story_id)
            for topic in topics:
                res.append(topic.toJSON())

            return createSuccessResponse(
                story[0].toJSON(
                    topics=res,
                    reposted=reposted,
                    favorited=favorited,
                    user=story[1].toJSON(),
                    reposts=story[2],
                    favorites=story[3]
                )
            )
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except StoryNotFoundException:
            return createErrorResponse(StoryNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def createStory(cls, auth, request):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            story = StoryRepository.create(request['title'], user.user_id, request['content'])
            for topic in request['topics']:
                queryTopic = TagRepository.getTag(topic['tag_id'])
                if queryTopic is not None:
                    StoryTagRepository.create(story.story_id, topic['tag_id'])

            friends = UserRepository.getFriends(userId)
            for friend in friends:
                UserNotificationRepository.create(friend[0].user_id, userId, 4)

            return createSuccessResponse("crated")
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getStories(cls, userId, auth):
        try:
            user = UserRepository.getUserById(auth['user_id'])

            if user is None:
                raise UnAuthorizedException()

            stories = StoryRepository.getStories(userId)
            res = []
            for story in stories:
                reposted = RepostRepository.getRepost(user.user_id, story[0].story_id) is not None
                favorited = FavoriteRepository.getFavorite(user.user_id, story[0].story_id) is not None
                topics = StoryTagRepository.getTags(story[0].story_id)
                is_page_user_owner = userId == story[0].user_id
                is_requesting_user_owner = user.user_id == story[0].user_id
                resTopics = []
                for topic in topics:
                    resTopics.append(topic.toJSON())
                res.append(
                    story[0].toJSON(
                        is_page_user_owner=is_page_user_owner,
                        is_requesting_user_owner=is_requesting_user_owner,
                        topics=resTopics,
                        reposted=reposted,
                        favorited=favorited,
                        user=story[1].toJSON(),
                        reposts=story[2],
                        favorites=story[3]
                    )
                )
            return createSuccessResponse(res)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getFavoriteStories(cls, userId, auth):
        try:
            user = UserRepository.getUserById(auth['user_id'])

            if user is None:
                raise UnAuthorizedException()

            stories = StoryRepository.getFavoriteStories(userId)
            res = []
            for story in stories:
                reposted = RepostRepository.getRepost(user.user_id, story[0].story_id) is not None
                topics = StoryTagRepository.getTags(story[0].story_id)
                own = userId == story[0].user_id
                resTopics = []
                for topic in topics:
                    resTopics.append(topic.toJSON())
                res.append(
                    story[0].toJSON(
                        own=own,
                        topics=resTopics,
                        reposted=reposted,
                        favorited=True,
                        user=story[1].toJSON(),
                        reposts=story[2],
                        favorites=story[3]
                    )
                )

            return createSuccessResponse(res)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

