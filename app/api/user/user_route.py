from . import user_bp
from app.entity.User import User
from app.util.Resp import mk_resp
from app import logger
from app.service.UserService import user_service


@user_bp.route('/')
def find_list():
    logger.info('List users.')
    return mk_resp(data=User.query.all())


@user_bp.route('/<user_id>')
def find_by_id(user_id):
    logger.info('Find users by id: %s.' % user_id)
    return mk_resp(data=user_service.find_by_id(user_id))


@user_bp.route('/username/<username>')
def find_by_name(username):
    logger.info('Find users by username: %s.' % username)
    return mk_resp(data=user_service.find_by_username(username))
