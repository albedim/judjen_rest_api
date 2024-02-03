import datetime
import os
from datetime import timedelta

import jwt

from flask import send_file
from flask_jwt_extended import create_access_token
from app.model.repository.user import UserRepository
from app.utils.errors.FileNotFoundEcxeption import FileNotFoundException
from app.utils.errors.GException import GException
from app.utils.errors.InvalidSchemaException import InvalidSchemaException
from app.utils.errors.TokenExpiredException import TokenExpiredException
from app.utils.errors.UnAuthotizedException import UnAuthorizedException
from app.utils.errors.UserAlreadyExistsException import UserAlreadyExistsException
from app.utils.errors.UserNotFoundException import UserNotFoundException
from app.utils.utils import createSuccessResponse, createErrorResponse, hashString, saveFile


class UserService:

    @classmethod
    def getUser(cls, userId):
        try:
            user = UserRepository.getUserById(userId)
            if user is None:
                raise UserNotFoundException()
            return createSuccessResponse(user.toJSON())
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            return createErrorResponse(GException(exc))

    @classmethod
    def signin(cls, request):
        try:
            user = UserRepository.getUserByEmail(request['email'])

            if user is None:
                raise UserNotFoundException()
            if user.password == hashString(request['password']):
                return createSuccessResponse({
                    'token': create_access_token(identity={'user_id': user.user_id, 'expires_in': 14}, expires_delta=timedelta(days=14))
                })
            else:
                raise UserNotFoundException()

        except UserNotFoundException as exc:
            return createErrorResponse(UserNotFoundException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def sync(cls, tokenSub):
        try:
            user = UserRepository.getUserById(tokenSub['user_id'])
            if user is None:
                raise UserNotFoundException()
            return createSuccessResponse(True)
        except UserNotFoundException:
            return createErrorResponse(UserNotFoundException())
        except jwt.exceptions.ExpiredSignatureError:
            return createErrorResponse(TokenExpiredException())
        except jwt.exceptions.DecodeError:
            return createErrorResponse(UnAuthorizedException())
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def signup(cls, request):
        try:
            user = UserRepository.getUserByEmail(request['email'])

            if user is not None:
                raise UserAlreadyExistsException()

            user = UserRepository.create(
                request['email'],
                hashString(request['password'])
            )
            return createSuccessResponse({
                'token': create_access_token(identity={'user_id': user.user_id, 'expires_in': 14},
                                             expires_delta=timedelta(days=14))
            })

        except UserAlreadyExistsException as exc:
            return createErrorResponse(UserAlreadyExistsException)
        except KeyError as exc:
            return createErrorResponse(InvalidSchemaException)
        except Exception as exc:
            print(exc)
            return createErrorResponse(GException(exc))

    @classmethod
    def getMatchingUsers(cls, auth, name):
        user = UserRepository.getUserById(auth['user_id'])
        if user is None:
            raise UserNotFoundException()

        users = UserRepository.getUsers(user.user_id, name)
        res = []
        for user in users:
            res.append(user.toJSON())
        return createSuccessResponse(res)
