from app.configuration.config import sql
from app.model.repository.repo import Repository
from app.model.entity.friend import Friend

class FriendRepository(Repository):

    @classmethod
    def create(cls, userId, friendId):
        friend = Friend(userId, friendId)
        sql.session.add(friend)
        sql.session.commit()

    @classmethod
    def remove(cls, userId, friendId):
        friend = sql.session.query(Friend).filter(Friend.user_id == userId).filter(Friend.friend_id == friendId).delete()
        sql.session.commit()

    @classmethod
    def get(cls, userId, friendId):
        friend = sql.session.query(Friend).filter(Friend.user_id == userId).filter(
            Friend.friend_id == friendId).first()
        return friend