from app.util.Resp import success
from app import logger
from app.service.UserService import user_service
from . import user_bp as api
from app.vo.UserVO import UserVO
from app.util.JwtUtils import decode_auth_token
from app.security import token_auth
from app import APPLICATION_CONFIG
from flask import request
from app.exception.LoginException import LoginException


@api.route('/list', methods=['GET'])
@token_auth.login_required
def list_user():
    logger.info('List users.')
    return success(data=user_service.find_list())


@api.route('/<string:user_id>', methods=['GET'])
@token_auth.login_required
def find_by_id(user_id):
    logger.info('List users.')
    return success(data=user_service.find_by_id(user_id))


@api.route('', methods=['POST'])
@token_auth.login_required
def add_one():
    logger.info('Add user.')
    return success(data=user_service.add())


@api.route('/<string:user_id>', methods=['DELETE'])
@token_auth.login_required
def delete_one(user_id):
    logger.info('Delete user.')
    user_service.delete(user_id)
    return success()


@api.route('/username/<string:username>', methods=['GET'])
@token_auth.login_required
def find_by_username(username):
    logger.info('List users.')
    return success(data=user_service.find_by_username(username))


@api.route('/info', methods=['GET'])
@token_auth.login_required
def find_info():
    token = request.headers[APPLICATION_CONFIG['jwt'].get('header_key', 'Authorization')]
    payload = decode_auth_token(token)
    user_info = user_service.find_by_username(payload['data']['username'])
    return success(data=UserVO.convert(user_info))
