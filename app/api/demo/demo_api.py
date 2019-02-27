from . import demo_bp
from app.entity.User import User
from app.util.JsonUtils import AlchemyEncoder
import json


@demo_bp.route('/')
def demo():
    return 'hello'
