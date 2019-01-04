# coding=utf-8
import logging

from flask import request
from flask_restplus import Resource, fields, marshal_with
from webargs import fields as f
from webargs.flaskparser import use_args

from src.extensions.namespace import Namespace
from src.helpers.response_helper import api_response
from src.model.user import User, UserSchema

__author__ = 'ThucNC'
_logger = logging.getLogger(__name__)

ns = Namespace('user', description='User operations')

_user = ns.model('user', UserSchema.user)
_user_post = ns.model('user_post', UserSchema.user_post)


@ns.route('', methods=['GET', 'POST'])
class UserApi(Resource):
    """
    Hello world api
    """
    def get(self):
        _logger.warn('User API: {}')
        # return api_response(request.args, 'ok', 200)
        return request.args, 200

    @ns.doc(description='Create an user')
    @ns.expect(_user_post, validate=True)
    @ns.marshal_with(_user)
    def post(self):
        data = request.json
        user = User(**data)
        # user.password = data['password']
        return user

