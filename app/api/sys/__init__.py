from flask import Blueprint
from app.api import context_path

sys_bp = Blueprint('sys', __name__, url_prefix='%s/sys' % context_path)

