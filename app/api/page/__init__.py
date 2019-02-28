from flask import Blueprint

page_bp = Blueprint('page', __name__, url_prefix='/p')

from . import page_api
