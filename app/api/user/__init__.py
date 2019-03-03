from flask import Blueprint

user_bp = Blueprint(__name__, __name__,
                    url_prefix='/api/user')

from . import user_route
