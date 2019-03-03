from flask import request
from app.exception.AuthException import AuthException
from app.service.UserService import user_service
from app.util.Resp import success
from app.util import JwtUtils
from . import auth_bp
from app.auth import basic_auth, token_auth

AUTHORIZATION = 'Authorization'


@auth_bp.route('/token', methods=['POST', 'GET'])
@basic_auth.login_required
def authenticate():
    username_auth = request.authorization.get('username') if request.authorization else None
    user = user_service.find_by_username(username_auth or request.form['username'])
    return success(data=JwtUtils.encode_auth_token(user.id, user.username))


@auth_bp.route('/identify', methods=['get'])
@token_auth.login_required
def identify():
    return success()


@auth_bp.route('/forbidden', methods=['get'])
@token_auth.login_required
def forbidden():
    raise AuthException('无权限')
