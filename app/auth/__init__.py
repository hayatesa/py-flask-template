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
    :return: boolean
    """
    data = request.json
    _username = username or data.get('username')
    _password = password or data.get('password')
    if not _username:
        abort(401, **{'description': '认证失败: 请提供用户名'})
    if not _password:
        abort(401, **{'description': '认证失败: 请提供密码'})

    user_info = user_service.find_by_username(_username)
    if not user_info:
        abort(401, **{'description': '认证失败: 用户不存在'})
    if not check_password_hash(user_info.password, _password):
        abort(401, **{'description': '认证失败: 密码错误'})
    user_info.lastAccessTime = datetime.datetime.now()
    user_service.update(user_info)
    return True


@token_auth.verify_token
def verify_token(token):
    if not token:
        abort(401, **{'description': '禁止访问: 令牌缺失'})

    try:
        payload = JwtUtils.decode_auth_token(token)
        if not JwtUtils.is_valid_token(payload):
            raise TokenException('禁止访问: 令牌无效')
        if JwtUtils.is_token_expired(payload['exp']):
            abort(401, **{'description': '禁止访问: 令牌过期'})
    except TokenException as e:
        abort(401, **{'description': e.message})
    return True
