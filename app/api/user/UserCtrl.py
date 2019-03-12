from app.util.Resp import success
from app import logger
from app.service.UserService import user_service
from . import user_bp as api
from flask import request


@api.route('/list', methods=['GET'])
def list_user():
    logger.info('List users.')
    return success(data=user_service.find_list())

#
# @api.route('/<string:id>', methods=['GET'])
# def find_by_id(id):
#     logger.info('List users.')
#     return success(data=user_service.find_by_id(id))


@api.route('', methods=['POST'])
def add_one():
    logger.info('Add user.')
    return success(data=user_service.add(id))


@api.route('/<string:id>', methods=['DELETE'])
def delete_one():
    logger.info('Delete user.')
    user_service.delete(id)
    return success()


@api.route('/username/<string:username>', methods=['GET'])
def find_by_username(username):
    logger.info('List users.')
    return success(data=user_service.find_by_username(username))


@api.route('/info', methods=['GET'])
def find_info():
    r = request
    logger.info('List users.')
    return success(data=user_service.find_by_username('kimi'))
