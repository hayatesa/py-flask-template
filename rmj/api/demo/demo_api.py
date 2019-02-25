from . import demo_bp
from rmj.entity.User import User
from rmj.util.JsonUtils import AlchemyEncoder
import json


@demo_bp.route('/')
def demo():
    return 'hello'
