#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import sqlalchemy_config, log_config, web_config
import os
import sys
import time
import logging

db = SQLAlchemy()
app = Flask(__name__, static_folder='templates')


def make_dir(dir_path):
    _path = dir_path.strip()
    if not os.path.exists(_path):
        os.makedirs(_path)
    #     logging.info('Make directory: ' + _path)
    # else:
    #     logging.info(_path + 'already exists.')
    return _path


def __init_log():
    with open('%s/banner.txt' % sys.path[0], 'r') as f:
        banner = f.read()
        print(banner)

    _default_log_config = {
        'path': sys.path[0],
        'filename': '%s.log' % __name__,
        'format': '%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(funcName)s: %(message)s',
        'date_fmt': '%Y-%m-%d %H:%M:%S',
        'filemode': 'a',
        'level': logging.DEBUG
    }

    _log_config = log_config()

    _level = _log_config.get('level', _default_log_config['level'])
    _format = _log_config.get('format', _default_log_config['format'])
    _datefmt = _log_config.get('date_fmt', _default_log_config['date_fmt'])

    _path = make_dir(_log_config.get('path', _default_log_config['path']))
    _filename = _log_config.get('filename', _default_log_config['filename'])
    _file_path = os.path.join(_path, _filename)

    _filemode = _log_config.get('filemode', _default_log_config['filemode'])

    logging.basicConfig(level=_level,
                        format=_format,
                        datefmt=_datefmt,
                        filename=_file_path,
                        filemode=_filemode)
    with open(_file_path, 'a') as f:
        f.write(banner)

    logging.info('Complete log config.')


def __init_db():
    # if if_create_db():
    #     db.create_all()
    db.init_app(app)
    # logging.info('Complete db init.')


def __init_app():
    app.config.from_mapping(sqlalchemy_config())
    cors = web_config()
    # CORS(app, supports_credentials=cors['supports_credentials'],
    #      resources={cors['resources']['path']: {"origins": cors['resources']['origins']}})
    logging.info('Complete app init.')


def __init_route():
    from rmj.api.demo import demo_bp
    from rmj.api.user import user_bp
    from rmj.api.page import page_bp
    app.register_blueprint(demo_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(page_bp)
    logging.info('Complete route config.')


if __name__ == '__main__':
    __init_log()
    __init_app()
    __init_db()
    __init_route()
    app.run(debug=True)
    time_end = time.time()
