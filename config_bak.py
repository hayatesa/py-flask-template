PROFILE = {
    'dev': {
        'init_db': True,
        'sqlalchemy': {
            'SQLALCHEMY_DATABASE_URI': 'mysql://dev:dev@119.29.94.246:3306/test_db?charset=utf8',
            'SQLALCHEMY_TRACK_MODIFICATIONS': True,
            'SQLALCHEMY_ECHO': True
        },
        'log': {
            'path': 'D:/AppLog',
            'filename': 'app.log',
            'format': '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s'
        },
        'cors': {
            'supports_credentials': True,
            'resources': {
                'path': r'/api/*',
                'origins': '*'
            }
        }
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


def sqlalchemy_config(profile):
    return PROFILE[profile]['sqlalchemy']


def log_config(profile):
    return PROFILE[profile]['log']


def if_create_db(profile):
    return PROFILE[profile]['init_db']


def cors_config(profile):
    return PROFILE[profile]['cors']
