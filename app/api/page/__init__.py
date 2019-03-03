from flask import Blueprint

page_bp = Blueprint('p', __name__, url_prefix='')

from . import page_api
