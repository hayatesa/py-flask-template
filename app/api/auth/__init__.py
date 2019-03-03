from flask import Blueprint
from app import APPLICATION_CONFIG

auth_bp = Blueprint(__name__, __name__, url_prefix='%s/auth' % APPLICATION_CONFIG['server'].get('context_path', ''))

from . import AuthCtrl
