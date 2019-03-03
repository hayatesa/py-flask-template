from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
from flask import request, abort
from werkzeug.security import check_password_hash
from app.service.UserService import user_service
from app.exception.TokenException import TokenException
import datetime

from app.util import JwtUtils

basic_auth = HTTPBasicAuth()
token_auth = HTTPTokenAuth()


@basic_auth.verify_password
def verify_password(username, password):
    """
    验证用户名密码
    :param username:  用户名 来自URL组件或POST请求参数
    :param password: 密码 来自URL组件或POST请求参数
    :return:
    """
    _username = username or request.form['username']
    _password = password or request.form['password']
    user_info = user_service.find_by_username(_username)
    if user_info is None:
        abort(401, **{'description': '认证失败, 用户不存在'})
    if not check_password_hash(user_info.password, _password):
        abort(401, **{'description': '认证失败, 密码错误'})
    user_info.lastAccessTime = datetime.datetime.now()
    user_service.update(user_info)
    return True


@token_auth.verify_token
def verify_token(token):
    if not token:
        abort(403, **{'description': '授权失败, Token缺失'})

    try:
        payload = JwtUtils.decode_auth_token(token)
        if not JwtUtils.is_valid_token(payload):
            raise TokenException('授权失败, Token无效')
        if JwtUtils.is_token_expired(payload['exp']):
            raise TokenException('授权失败, Token过期')
    except TokenException as e:
        abort(403, **{'description': e.message})
    return True