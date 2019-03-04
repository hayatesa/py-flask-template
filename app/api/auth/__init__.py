from flask import Blueprint
from flask_restplus import Api
from app.api import authorizations, version, context_path
from app.api.auth.AuthCtrl import auth_api

auth_bp = Blueprint('auth', __name__, url_prefix='%s/auth' % context_path)
api = Api(auth_bp, version=version, title='Auth API', authorizations=authorizations)

api.add_namespace(auth_api)
