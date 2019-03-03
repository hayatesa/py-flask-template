from flask import request, abort

from app.exception.TokenException import TokenException
from app.service.UserService import user_service
from app.util.Resp import success, failure
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
