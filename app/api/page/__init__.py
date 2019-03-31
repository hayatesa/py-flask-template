# -*- coding: utf-8 -*-
from flask import Blueprint

page_bp = Blueprint('page', __name__, url_prefix='')

from app.api.page import page_api
