from flask import Blueprint
from flask_restplus import Api

from app import APPLICATION_CONFIG

desc="""
    resource token, identify, forbidden, error
"""

auth_bp = Blueprint('auth', __name__, url_prefix='%s/auth' % APPLICATION_CONFIG['server'].get('context_path', ''))
api = Api(auth_bp, version=APPLICATION_CONFIG.get('version'), title='Auth RESTful API', desc=desc)
api.add_namespace()
from . import AuthCtrl
