from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
import sys
import time
import logging.config
from yaml import load

start_time = time.time()

CONTEXT_PATH = sys.path[0]  # 应用上下文路径

RESOURCES_PATH = os.path.join(CONTEXT_PATH, 'resources')  # 资源文件路径

CONF_FILE_INFO = {'path': 'config', 'filename': 'application', 'suffix': '.yml'}
CONFIG_FILE_PATH = os.path.join(RESOURCES_PATH, '%s/%s%s' % (CONF_FILE_INFO['path'],
                                                             CONF_FILE_INFO['filename'],
                                                             CONF_FILE_INFO['suffix']))  # 应用配置文件路径

LOG_CONF_FILE_INFO = {'path': 'log', 'filename': 'log', 'suffix': '.yml'}
LOG_CONF_PATH = os.path.join(RESOURCES_PATH, '%s/%s%s' % (LOG_CONF_FILE_INFO['path'],
                                                          LOG_CONF_FILE_INFO['filename'],
                                                          LOG_CONF_FILE_INFO['suffix']))  # 日志配置文件路径

BANNER_PATH = os.path.join(RESOURCES_PATH, 'banner.txt')  # banner路径


def __load_config__():
    app_config = {}
    _logger = logging.getLogger()
    _logger.setLevel(logging.DEBUG)
    if os.path.exists(CONFIG_FILE_PATH):
        try:
            with open(CONFIG_FILE_PATH, encoding='UTF-8') as f:
                conf = load(f)
                app_config = dict(app_config, **conf) if conf else app_config
        except Exception as e:
            _logger.error(e)
            sys.exit(1)
    else:
        _logger.error('无法找到文件%s' % CONFIG_FILE_PATH)
        sys.exit(1)

    profile = app_config.get('profile')
    # 如果指定了profile, 加载profile配置文件
    if profile:
        profile_path = os.path.join(RESOURCES_PATH, '%s/%s-%s%s' % (CONF_FILE_INFO['path'],
                                                                    CONF_FILE_INFO['filename'],
                                                                    profile,
                                                                    CONF_FILE_INFO['suffix']))
        if os.path.exists(profile_path):
            try:
                with open(profile_path, encoding='UTF-8') as f:
                    conf = load(f)
                    app_config = dict(app_config, **conf) if conf else app_config
            except Exception as e:
                _logger.error(e)
                sys.exit(1)
        else:
            _logger.warning('无法找到文件%s, 请检查profile拼写是否有误' % profile_path)

    return app_config


def __create_logger__():
    log_conf = {}
    if os.path.exists(LOG_CONF_PATH):
        with open(LOG_CONF_PATH, encoding='UTF-8') as f:
            log_conf = load(f)
            log_conf['version'] = log_conf.get('version') or 1

    profile = APPLICATION_CONFIG.get('profile')
    # 如果指定了profile, 加载profile配置文件
    if profile:
        profile_path = os.path.join(RESOURCES_PATH, '%s/%s-%s%s' % (LOG_CONF_FILE_INFO['path'],
                                                                    LOG_CONF_FILE_INFO['filename'],
                                                                    profile,
                                                                    LOG_CONF_FILE_INFO['suffix']))
        if os.path.exists(profile_path):
            try:
                with open(profile_path, encoding='UTF-8') as f:
                    conf = load(f)
                    log_conf = dict(log_conf, **conf) if conf else log_conf
            except Exception as e:
                logging.getLogger().error(e)
                sys.exit(1)
        else:
            logging.getLogger().warning('无法找到文件%s, 请检查profile拼写是否有误' % profile_path)

    logging.config.dictConfig(log_conf)
    _app_logger = logging.getLogger('app')
    return _app_logger


def __create_db__(flask_app):
    _db = SQLAlchemy()
    _db.init_app(flask_app)
    return _db


def __create_app__():
    flask_app = Flask(__name__, static_folder=os.path.join(
        CONTEXT_PATH,
        APPLICATION_CONFIG['server'].get('static_folder', 'templates')
    ))
    flask_app.config.from_mapping(APPLICATION_CONFIG.get('sqlalchemy', {}))
    __init_cors__(flask_app)
    return flask_app


def __init_cors__(flask_app):
    cors = APPLICATION_CONFIG.get('server').get('cors')
    supports_credentials = cors.get('allow') is True
    origins = (cors.get('origins') if cors.get('origins') else '*') if supports_credentials else ''
    path = (cors.get('path') if cors.get('path') else '/*') if supports_credentials else ''
    CORS(flask_app, supports_credentials=supports_credentials,
         resources={path: {"origins": origins}})


def __assemble_blueprint__(flask_app):
    from app.api.auth import auth_bp
    from app.api.user import user_bp
    from app.api.page import page_bp
    from app.api.test import test_bp
    flask_app.register_blueprint(auth_bp)
    flask_app.register_blueprint(user_bp)
    flask_app.register_blueprint(page_bp)
    flask_app.register_blueprint(test_bp)


def __register_api__():
    from app.api.test.route import ns as test_ns
    from app.api.test import test_api
    test_api.add_namespace(test_ns)


def message():
    if os.path.exists(BANNER_PATH):
        logger.info('Load banner.txt from %s' % BANNER_PATH)
        with open(BANNER_PATH, encoding='UTF-8') as f:
            logger.info(f.read())
    logger.info('Application launched in %.2f Seconds.' % (end_time - start_time))


APPLICATION_CONFIG = __load_config__()
logger = __create_logger__()
app = __create_app__()
db = __create_db__(app)
__register_api__()
__assemble_blueprint__(app)

end_time = time.time()
message()
