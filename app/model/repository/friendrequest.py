from app.configuration.config import sql
from app.model.repository.repo import Repository
from app.model.entity.friendrequest import FriendRequest

class FriendRequestRepository(Repository):

    @classmethod
    def create(cls, userId, targetId):
        friendRequest = FriendRequest(userId, targetId)
        sql.session.add(friendRequest)
        sql.session.commit()

    @classmethod
    def remove(cls, userId, targetId):
        friendRequest = sql.session.query(FriendRequest).filter(FriendRequest.user_id == userId).filter(FriendRequest.target_id == targetId).delete()
        sql.session.commit()

    @classmethod
    def get(cls, userId, targetId):
        friendRequest = sql.session.query(FriendRequest).filter(FriendRequest.user_id == userId).filter(FriendRequest.target_id == targetId).first()
        return friendRequest