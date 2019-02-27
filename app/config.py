profile = 'dev'

PROFILE = {
    'dev': {
        'web': {
            'cors': {
                'allow': True,
                'origins': '*',
                'path': ''
            }
        },
        'db': {
            'create': True,
        },
        'sqlalchemy': {
            'SQLALCHEMY_DATABASE_URI': 'mysql://dev:dev@119.29.94.246:3306/test_db?charset=utf8',
            'SQLALCHEMY_TRACK_MODIFICATIONS': True,
            'SQLALCHEMY_ECHO': True
        },
        'log': {
            'path': 'D:/AppLog',
            'filename': 'app.log',
            'format': '%(asctime)s %(levelname)s %(filename)s[%(lineno)d] %(funcName)s: %(message)s',
            'date_fmt': '%Y-%m-%d %H:%M:%S',
            'filemode': 'a'
        },

    },
    'prod': {
        'sqlalchemy': {
            'SQLALCHEMY_DATABASE_URI': 'mysql://dev:dev@119.29.94.246:3306/test_db?charset=utf8',
            'SQLALCHEMY_TRACK_MODIFICATIONS': True,
            'SQLALCHEMY_ECHO': True,
            'SQLALCHEMY_POOL_SIZE': 50,
            'SQLALCHEMY_POOL_TIMEOUT': 20
        },
        'log': {
            'path': '',
            'filename': '',
            'format': ''
        },

    }
}


def sqlalchemy_config():
    return PROFILE[profile].get('sqlalchemy')


def log_config():
    return PROFILE[profile].get('log')


def if_create_db():
    return PROFILE[profile].get('init_db')


def web_config():
    return PROFILE[profile].get('web')
