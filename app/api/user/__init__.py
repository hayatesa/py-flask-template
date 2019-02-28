from flask import Blueprint
from flask_restplus import Api

user_bp = Blueprint('user', __name__, url_prefix='/api/user')
user_api = Api(user_bp, version="1.0",
               prefix="/v1", title="User Api", description="User Restful API")

from . import user_route
