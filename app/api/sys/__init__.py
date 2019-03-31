# -*- coding: utf-8 -*-
from flask import Blueprint
from app.api import context_path

sys_bp = Blueprint('sys', __name__, url_prefix='%s/sys' % context_path)

from app.api.sys import sys_info_api
