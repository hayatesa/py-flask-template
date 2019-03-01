from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from app.config import sqlalchemy_config, web_config
import os
import sys
import time
import logging.config
from yaml import load

APP_CONFIG = {}

start_time = time.time()

CONTEXT_PATH = sys.path[0]  # 应用上下文路径

RESOURCES_FOLDER = 'resources'  # 资源文件夹
RESOURCES_PATH = os.path.join(CONTEXT_PATH, RESOURCES_FOLDER)  # 资源文件路径

LOG_FILE_NAME = 'log/log.yml'  # 日志配置文件名
LOG_CONF_PATH = os.path.join(RESOURCES_PATH, LOG_FILE_NAME)  # 日志配置文件路径

BANNER_FILE_NAME = 'banner.txt'  # banner文本文件名
BANNER_PATH = os.path.join(RESOURCES_PATH, BANNER_FILE_NAME)  # banner路径


def __create_logger__():
    if os.path.exists(LOG_CONF_PATH):
        with open(LOG_CONF_PATH) as f:
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
    __after_request__(flask_app)
    return flask_app


def __assemble_blueprint__(flask_app):
    from app.api.demo import demo_bp
    from app.api.user import user_bp
    from app.api.page import page_bp
    from app.api.test import test_bp
    flask_app.register_blueprint(demo_bp)
    flask_app.register_blueprint(user_bp)
    flask_app.register_blueprint(page_bp)
    flask_app.register_blueprint(test_bp)


def __register_api__():
    from app.api.user.user_route import ns as user_ns
    from app.api.user import user_api
    user_api.add_namespace(user_ns)

    from app.api.test.route import ns as test_ns
    from app.api.test import test_api
    test_api.add_namespace(test_ns)


def __after_request__(flask_app):
    @flask_app.after_request
    def after_request(response):
        # response.headers.add('Access-Control-Allow-Origin', '*')
        if request.method == 'OPTIONS':
            response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
            headers = request.headers.get('Access-Control-Request-Headers')
            if headers:
                response.headers['Access-Control-Allow-Headers'] = headers
        return response


def message():
    if os.path.exists(BANNER_PATH):
        logger.info('Loading banner.txt from')
        with open(BANNER_PATH) as f:
            logger.info(f.read())
    logger.info('Application launched in %.2f Seconds.' % (end_time - start_time))


logger = __create_logger__()
app = __create_app__()
db = __create_db__(app)
__register_api__()
__assemble_blueprint__(app)

end_time = time.time()
message()
