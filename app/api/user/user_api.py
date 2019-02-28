from . import user_bp
from app.entity.User import User
from app.util.Resp import mk_resp
from app import logger
from app.service import UserService


@user_bp.route('/', methods=['GET'])
def find_list():
    logger.info('List users.')
    return mk_resp(data=User.query.all())


@user_bp.route('/<user_id>', methods=['GET'])
def find_by_id(user_id):
    logger.info('Find users by id: %s.' % user_id)
    return mk_resp(data=UserService.find_by_id(user_id))


@user_bp.route('username/<username>', methods=['GET'])
def find_by_name(username):
    logger.info('Find users by username: %s.' % username)
    return mk_resp(data=UserService.find_by_username(username))
