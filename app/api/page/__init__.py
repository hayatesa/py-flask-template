from flask import Blueprint

page_bp = Blueprint('page', __name__, url_prefix='')

from . import page_api
