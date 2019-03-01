from flask import Blueprint
from flask_restplus import Api
from app import APP_CONFIG

user_bp = Blueprint(__name__, __name__,
                    url_prefix='%s/user' % APP_CONFIG.get('context-path', ''))

user_api = Api(user_bp,
               version=APP_CONFIG.get('version', ''),
               prefix='',
               title='User Api',
               description='User Restful API')

from . import user_route
