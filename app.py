#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import sqlalchemy_config, log_config, if_create_db
import os
import logging

# 对应config的PROFILE
PROFILE = 'dev'

db = SQLAlchemy()
app = Flask(__name__, static_folder='templates')


def __init_log():
    _log_config = log_config(PROFILE)
    path = _log_config['path']
    filename = _log_config['filename']
    log_file_path = os.path.join(path, filename)
    if not os.path.exists(path):
        os.makedirs(path)
    logging.basicConfig(filename=log_file_path, format=_log_config['format'])


def __init_db():
    # if if_create_db(PROFILE):
    #     db.create_all()
    db.init_app(app)


def __init_app():
    app.config.from_mapping(sqlalchemy_config(PROFILE))

    CORS(app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})


def __init_route():
    from rmj.api.demo import demo_bp
    from rmj.api.user import user_bp
    from rmj.api.page import page_bp
    app.register_blueprint(demo_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(page_bp)


if __name__ == '__main__':
    __init_log()
    __init_app()
    __init_db()
    __init_route()
    app.run(debug=True)
