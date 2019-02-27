#!/usr/bin/env python
# -*-coding:utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from config import sqlalchemy_config, log_config, web_config
import os
import sys
import logging


def make_dir(dir_path):
    _path = dir_path.strip()
    if not os.path.exists(_path):
        os.makedirs(_path)
    #     logging.info('Make directory: ' + _path)
    # else:
    #     logging.info(_path + 'already exists.')
    return _path


def __init_log__():
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
    _log_file_path = os.path.join(_path, _filename)
    _filemode = _log_config.get('filemode', _default_log_config['filemode'])

    # 创建一个日志器logger并设置其日志级别为DEBUG
    _logger = logging.getLogger()
    _logger.setLevel(_level)

    # 创建一个流处理器handler并设置其日志级别为DEBUG
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setLevel(_level)
    file_handler = logging.FileHandler(_log_file_path)
    file_handler.setLevel(_level)

    # 创建一个格式器formatter并将其添加到处理器handler
    formatter = logging.Formatter(_format)
    file_handler.setFormatter(formatter)
    stdout_handler.setFormatter(formatter)

    # 添加handler
    if not _logger.hasHandlers():
        _logger.addHandler(file_handler)
        _logger.addHandler(stdout_handler)

    with open('%s/banner.txt' % sys.path[0]) as f:
        banner = f.read()
        print(banner)
    with open(_log_file_path, 'w') as f:
        f.write(banner)

    return _logger


def __init_db__(flask_app):
    # if if_create_db():
    #     db.create_all()
    _db = SQLAlchemy()
    _db.init_app(flask_app)
    return _db


def __init_app__():
    flask_app = Flask(__name__, static_folder='templates')
    flask_app.config.from_mapping(sqlalchemy_config())

    # 跨域设置
    cors = web_config()
    allow = cors.get('allow')
    supports_credentials = allow is not None and allow
    origins = ('*' if cors.get('origins') is None else cors.get('origins')) if supports_credentials else ''
    path = ('/*' if cors.get('path') is None else cors.get('path')) if supports_credentials else ''
    CORS(app, supports_credentials=supports_credentials,
         resources={path: {"origins": origins}})
    return flask_app


def __init_route__(flask_app):
    from rmj.api.demo import demo_bp
    from rmj.api.user import user_bp
    from rmj.api.page import page_bp
    flask_app.register_blueprint(demo_bp)
    flask_app.register_blueprint(user_bp)
    flask_app.register_blueprint(page_bp)


logger = __init_log__()
app = __init_app__()
db = __init_db__(app)

if __name__ == '__main__':
    __init_route__(app)
    app.run(debug=True, use_reloader=False)
