from sqlalchemy import text
from sqlalchemy.orm import aliased

from app.configuration.config import sql
from app.model.entity.friend import Friend
from app.model.entity.friendrequest import FriendRequest
from app.model.entity.user import User
from app.model.repository.repo import Repository
from app.utils.utils import generateUuid


class UserRepository(Repository):

    @classmethod
    def create(cls, email, password):
        user: User = User(email, password)
        sql.session.add(user)
        sql.session.commit()
        return user

    @classmethod
    def getUserByEmail(cls, email):
        user = sql.session.query(User).filter(User.email == email).first()
        return user

    @classmethod
    def getUserById(cls, user_id):
        user = sql.session.query(User).filter(User.user_id == user_id).first()
        return user

    @classmethod
    def signin(cls, email, password):
        user = sql.session.query(User).filter(User.email == email).filter(User.password == password).first()
        return user

    @classmethod
    def getFriends(cls, userId):
        friends = sql.session.query(User, text("friends.created_on"))\
                   .join(Friend, Friend.friend_id == User.user_id)\
                   .filter(Friend.user_id == userId).all()
        return friends

    @classmethod
    def getSentFriendRequests(cls, userId):
        friendRequests = sql.session.query(User, text("friendrequests.created_on")) \
            .join(FriendRequest, FriendRequest.target_id == User.user_id) \
            .filter(FriendRequest.user_id == userId).all()
        return friendRequests

    @classmethod
    def getReceivedFriendRequests(cls, userId):
        friendRequests = sql.session.query(User, text("friendrequests.created_on")) \
            .join(FriendRequest, FriendRequest.user_id == User.user_id) \
            .filter(FriendRequest.target_id == userId).all()
        return friendRequests

    @classmethod
    def getUsers(cls, userId, name):
        f1 = aliased(Friend)
        f2 = aliased(Friend)

        users = (
            sql.session.query(User)
            .outerjoin(f1, (User.user_id == f1.friend_id) & (f1.user_id == userId))
            .outerjoin(f2, (User.user_id == f2.user_id) & (f2.friend_id == userId))
            .filter(User.user_id != userId)
            .filter(f1.friend_id.is_(None))
            .filter(f2.user_id.is_(None))
            .filter(User.anonymous_name.like(f'%{name}%'))
            .all()
        )
        return users
