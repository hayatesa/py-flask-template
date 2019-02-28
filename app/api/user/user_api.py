from . import user_bp
from app.entity.User import User
from app.util.Resp import mk_resp
from app import logger


@user_bp.route('/', methods=['GET'])
def find_list():
    logger.info('List users')
    return mk_resp(data=User.query.all())


@user_bp.route('/<user_id>', methods=['GET'])
def find_by_id(user_id):
    return mk_resp(data=User.query.filter_by(id=user_id).all())


@user_bp.route('username/<username>', methods=['GET'])
def find_by_name(username):
    return mk_resp(data=User.query.filter_by(username=username).all())


@user_bp.route('/test', methods=['GET'])
def test():
    return mk_resp()