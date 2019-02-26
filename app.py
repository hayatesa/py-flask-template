#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import sqlalchemy_config, log_config, cors_config
import os
import logging

# 对应config的profile
profile = 'dev'

db = SQLAlchemy()
app = Flask(__name__, static_folder='templates')


def make_dir(make_dir_path):
    path = make_dir_path.strip()
    if not os.path.exists(path):
        os.makedirs(path)
    return path


def __init_log():
    _log_config = log_config(profile)
    logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        filename='/home/URL/client/test_log.log',
                        filemode='a')


def __init_db():
    # if if_create_db(profile):
    #     db.create_all()
    db.init_app(app)


def __init_app():
    app.config.from_mapping(sqlalchemy_config(profile))
    cors = cors_config(profile)
    CORS(app, supports_credentials=cors['supports_credentials'],
         resources={cors['resources']['path']: {"origins": cors['resources']['origins']}})


def __init_route():
    from rmj.api.demo import demo_bp
    from rmj.api.user import user_bp
    from rmj.api.page import page_bp
    app.register_blueprint(demo_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(page_bp)


if __name__ == '__main__':
    # __init_log()
    __init_app()
    __init_db()
    __init_route()
    app.run(debug=True)
