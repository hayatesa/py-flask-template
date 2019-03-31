# -*- coding: utf-8 -*-
from flask import Blueprint
from app.api import context_path

user_bp = Blueprint('user', __name__, url_prefix='%s/user' % context_path)

from app.api.user import user_api
