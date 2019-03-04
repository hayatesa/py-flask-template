from flask import Blueprint
from flask_restplus import Api
from app.api import authorizations, version, context_path
from app.api.sys.UserCtrl import user_api
from app.api.sys.SysInfoCtrl import sys_api

sys_bp = Blueprint('sys', __name__, url_prefix='%s/sys' % context_path)

api = Api(sys_bp, version=version, title='System API', authorizations=authorizations, security='bearerAuth')
api.add_namespace(user_api)
api.add_namespace(sys_api)
