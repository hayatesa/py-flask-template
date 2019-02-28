from app import logger
import os


def __make_dir__(dir_path):
    _path = dir_path.path.strip()
    if not os.path.exists(_path):
        os.makedirs(_path)
        logger.info('Make directory: ' + _path)
    else:
        logger.info(_path + 'already exists.')
    return _path
