from app.model.repository.repo import Repository
from app.model.repository.friend import FriendRepository
from app.model.repository.user import UserRepository
from app.utils.errors.FriendRequestNotFoundException import FriendRequestNotFoundException
from app.utils.errors.GException import GException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.utils import createSuccessResponse, createErrorResponse


class FriendService(Repository):

    @classmethod
    def getFriends(cls, auth):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            friends = UserRepository.getFriends(user.user_id)
            res = []
            for friend in friends:
                res.append(friend[0].toJSON(created_on=str(friend[1])))
            return createSuccessResponse({ 'received_friend_requests': len(UserRepository.getReceivedFriendRequests(userId)), 'friends': res })
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def remove(cls, auth, friendId):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            friend = FriendRepository.get(user.user_id, friendId)
            if friend is None:
                raise FriendRequestNotFoundException()

            FriendRepository.remove(user.user_id, friendId)
            FriendRepository.remove(friendId, user.user_id)
            return cls.getFriends(auth)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except FriendRequestNotFoundException:
            return createErrorResponse(FriendRequestNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))