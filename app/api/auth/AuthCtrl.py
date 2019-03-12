from flasgger import swag_from
from flask import request
from app.exception.AuthException import AuthException
from app.service.UserService import user_service
from app.util.Resp import success
from app.util import JwtUtils
from app.security import basic_auth, token_auth
from app import RESOURCES_PATH
from . import auth_bp as api


@api.route('/token', methods=['POST'])
@basic_auth.login_required
def token():
    username_auth = request.authorization.get('username') if request.authorization else None
    user = user_service.find_by_username(username_auth or request.json['username'])
    return success(data=JwtUtils.encode_auth_token(user.id, user.username))


@api.route('/logout', methods=['POST'])
def logout():
    return success()


@api.route('/test/identify', methods=['GET'])
@token_auth.login_required
def test_identify():
    return success()


@api.route('/test/error', methods=['GET'])
@token_auth.login_required
def test_error():
    raise Exception()


@swag_from('%s/docs/auth.yml' % RESOURCES_PATH)
@api.route('/test/exception', methods=['GET'])
@token_auth.login_required
def test_exception():
    raise AuthException('无权限')
