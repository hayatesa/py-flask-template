from app.util.Resp import success
from app import logger
from app.service.UserService import user_service
from . import sys_bp as api


@api.route('/list')
def list_user():
    logger.info('List users.')
    return success(data=user_service.find_list())


@api.route('/<string:id>')
def find_by_id(id):
    logger.info('List users.')
    return success(data=user_service.find_by_id(id))


@api.route('/<string:id>')
def add_one(id):
    logger.info('Add user.')
    return success(data=user_service.add(id))


@api.route('/<string:id>')
def delete_one(id):
    logger.info('Delete user.')
    user_service.delete(id)
    return success()


@api.route('/username/<string:username>')
def find_by_username(username):
    logger.info('List users.')
    return success(data=user_service.find_by_username(username))
