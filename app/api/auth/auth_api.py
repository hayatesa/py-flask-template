# -*- coding: utf-8 -*-
from flasgger import swag_from
from flask import request
from app.exception import AuthorizationException
from app.service import user_srv
from app.util.resp import success
from app.util import jwt_util
from app.api import basic_auth, token_auth
from app import RESOURCES_PATH

from app.api.auth import auth_bp as api


@api.route('/token', methods=['POST'])
@basic_auth.login_required
def token():
    username_auth = request.authorization.get('username') if request.authorization else None
    user = user_srv.find_by_username(username_auth or request.json['username'])
    return success(data=jwt_util.encode_auth_token(user.id, user.username))


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
    raise AuthorizationException('无权限')
