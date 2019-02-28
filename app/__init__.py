from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import sqlalchemy_config, log_config, web_config
import os
import sys
import time
import logging.config
from yaml import load

start_time = time.time()


def make_dir(dir_path):
    _path = dir_path.strip()
    if not os.path.exists(_path):
        os.makedirs(_path)
    #     logging.info('Make directory: ' + _path)
    # else:
    #     logging.info(_path + 'already exists.')
    return _path


def __create_logger__():
    log_conf_path = '%s/log.yml' % sys.path[0]

    if os.path.exists(log_conf_path):
        with open(log_conf_path) as f:
            conf = load(f)
        logging.config.dictConfig(conf)

    _app_logger = logging.getLogger('app')
    return _app_logger


def __create_db__(flask_app):
    # if if_create_db():
    #     db.create_all()
    _db = SQLAlchemy()
    _db.init_app(flask_app)
    return _db


def __create_app__():
    flask_app = Flask(__name__, static_folder='../templates')
    flask_app.config.from_mapping(sqlalchemy_config())

    # 跨域设置
    cors = web_config()
    allow = cors.get('allow')
    supports_credentials = allow is not None and allow
    origins = ('*' if cors.get('origins') is None else cors.get('origins')) if supports_credentials else ''
    path = ('/*' if cors.get('path') is None else cors.get('path')) if supports_credentials else ''
    CORS(flask_app, supports_credentials=supports_credentials,
         resources={path: {"origins": origins}})

    return flask_app


def __assemble_blueprint__(flask_app):
    from app.api.demo import demo_bp
    from app.api.user import user_bp
    from app.api.page import page_bp
    flask_app.register_blueprint(demo_bp)
    flask_app.register_blueprint(user_bp)
    flask_app.register_blueprint(page_bp)


def message():
    banner_path = '%s/banner.txt' % sys.path[0]
    if os.path.exists(banner_path):
        with open(banner_path) as f:
            logger.info(f.read())
    logger.info('Application launched in %.2f Seconds.' % (end_time - start_time))


logger = __create_logger__()
app = __create_app__()
db = __create_db__(app)
__assemble_blueprint__(app)

end_time = time.time()
message()
