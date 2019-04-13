# -*- coding: utf-8 -*-
from app.util.resp import success
from app import logger
from app.service import user_srv
from app.api.user import user_bp as api
from app.vo.user_vo import UserVO
from app.util.jwt_util import decode_auth_token
from app.api import token_auth
from app import APPLICATION_CONFIG
from flask import request


@api.route('/list', methods=['GET'])
@token_auth.login_required
def list_user():
    logger.info('List users.')
    return success(data=user_srv.find_list())


@api.route('/<string:user_id>', methods=['GET'])
@token_auth.login_required
def find_by_id(user_id):
    logger.info('List users.')
    return success(data=user_srv.find_by_id(user_id))


@api.route('', methods=['POST'])
@token_auth.login_required
def add_one():
    logger.info('Add user.')
    return success(data=user_srv.add())


@api.route('/<string:user_id>', methods=['DELETE'])
@token_auth.login_required
def delete_one(user_id):
    logger.info('Delete user.')
    user_srv.delete(user_id)
    return success()


@api.route('/username/<string:username>', methods=['GET'])
@token_auth.login_required
def find_by_username(username):
    logger.info('List users.')
    return success(data=user_srv.find_by_username(username))


@api.route('/info', methods=['GET'])
@token_auth.login_required
def find_info():
    token = request.headers[APPLICATION_CONFIG['jwt'].get('header_key', 'Authorization')]
    payload = decode_auth_token(token)
    user_info = user_srv.find_by_username(payload['data']['username'])
    return success(data=UserVO.convert(user_info))
