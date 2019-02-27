from flask import Blueprint


demo_bp = Blueprint('demo', __name__, url_prefix='/api/demo')

from . import demo_api
