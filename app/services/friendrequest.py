from app.model.repository.friend import FriendRepository
from app.model.repository.repo import Repository
from app.model.repository.friendrequest import FriendRequestRepository
from app.model.repository.user import UserRepository
from app.utils.errors.FriendRequestAlreadyExistsException import FriendRequestAlreadyExistsException
from app.utils.errors.FriendRequestNotFoundException import FriendRequestNotFoundException
from app.utils.errors.GException import GException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.utils import createSuccessResponse, createErrorResponse


class FriendRequestService(Repository):

    @classmethod
    def create(cls, auth, request):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)
            target = UserRepository.getUserById(request['friend_id'])

            if target is None or user is None or target.user_id == user.user_id:
                raise UnAuthorizedException()

            friendRequest = FriendRequestRepository.get(user.user_id, request['friend_id'])

            if friendRequest is not None:
                raise FriendRequestAlreadyExistsException()

            friend = FriendRequestRepository.create(user.user_id, request['friend_id'])
            return createSuccessResponse("friend request created")
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except FriendRequestAlreadyExistsException:
            return createErrorResponse(FriendRequestAlreadyExistsException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def accept(cls, auth, request):
        try:
            userId = auth['user_id']
            target = UserRepository.getUserById(userId)
            user = UserRepository.getUserById(request['user_id'])

            if target is None or user is None:
                raise UnAuthorizedException()

            friendRequest = FriendRequestRepository.get(user.user_id, target.user_id)
            if friendRequest is None:
                raise FriendRequestNotFoundException()

            if friendRequest.target_id != userId:
                raise UnAuthorizedException()

            friend = FriendRepository.create(friendRequest.user_id, friendRequest.target_id)
            friend = FriendRepository.create(friendRequest.target_id, friendRequest.user_id)
            FriendRequestRepository.remove(friendRequest.user_id, friendRequest.target_id)
            return createSuccessResponse("friend created")
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except FriendRequestNotFoundException:
            return createErrorResponse(FriendRequestNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def reject(cls, auth, request):
        try:
            userId = auth['user_id']
            target = UserRepository.getUserById(userId)
            user = UserRepository.getUserById(request['user_id'])

            if user is None or target is None:
                raise UnAuthorizedException()

            friendRequest = FriendRequestRepository.get(user.user_id, target.user_id)
            if friendRequest is None:
                raise FriendRequestNotFoundException()

            if friendRequest.target_id != userId:
                raise UnAuthorizedException()

            FriendRequestRepository.remove(user.user_id, target.user_id)
            return createSuccessResponse("friend request rejected")
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except FriendRequestNotFoundException:
            return createErrorResponse(FriendRequestNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getSentFriendRequests(cls, auth):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            friends = UserRepository.getSentFriendRequests(user.user_id)
            res = []
            for friend in friends:
                res.append(friend[0].toJSON(accepted=False, sent_on=str(friend[1])))
            return createSuccessResponse(res)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def getReceivedFriendRequests(cls, auth):
        try:
            userId = auth['user_id']
            user = UserRepository.getUserById(userId)

            if user is None:
                raise UnAuthorizedException()

            friends = UserRepository.getReceivedFriendRequests(user.user_id)
            res = []
            for friend in friends:
                res.append(friend[0].toJSON(received_on=str(friend[1])))
            return createSuccessResponse(res)
        except UnAuthorizedException:
            return createErrorResponse(UnAuthorizedException)
        except Exception as exc:
            return createErrorResponse(GException(exc))