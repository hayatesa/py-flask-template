from flask import Blueprint
from flask_restplus import Api
from app import APP_CONFIG

test_bp = Blueprint(__name__, __name__, url_prefix='%s/test' % APP_CONFIG.get('context-path', ''))

test_api = Api(test_bp,
               version=APP_CONFIG.get('version', ''),
               prefix='',
               title='Test Api',
               description='Test Restful API')
