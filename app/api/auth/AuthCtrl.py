from flask import request
from flask_restplus import Namespace, fields, Resource

from app.exception.AuthException import AuthException
from app.service.UserService import user_service
from app.util.Resp import success
from app.util import JwtUtils
from app.auth import basic_auth, token_auth

auth_api = Namespace('token', description='Token API')

auth_model = auth_api.model('auth', {
    'username': fields.String(),
    'password': fields.String()
})


@auth_api.route('')
class AuthApi(Resource):

    @basic_auth.login_required
    @auth_api.doc(security='basicAuth')
    @auth_api.expect(auth_model)
    def post(self):
        username_auth = request.authorization.get('username') if request.authorization else None
        user = user_service.find_by_username(username_auth or request.json['username'])
        return success(data=JwtUtils.encode_auth_token(user.id, user.username))


@auth_api.route('/test/identify')
class AuthIdentifyApi(Resource):

    @token_auth.login_required
    @auth_api.doc(security='bearerAuth')
    def get(self):
        return success()


@auth_api.route('/test/error')
class AuthErrorApi(Resource):
    @token_auth.login_required
    @auth_api.doc(security='bearerAuth')
    def get(self):
        raise Exception()


@auth_api.route('/test/exception')
class AuthExceptionApi(Resource):
    @token_auth.login_required
    @auth_api.doc(security='bearerAuth')
    def get(self):
        raise AuthException('无权限')
