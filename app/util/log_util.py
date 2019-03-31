# -*- coding: utf-8 -*-
import logging


class Logger:

    def __init__(self):
        self.logger = logging.getLogger('app')

    def debug(self, msg=''):
        self.logger.debug(msg)

    def info(self, msg=''):
        self.logger.info(msg)

    def warning(self, msg=''):
        self.logger.warning(msg)

    def error(self, msg=''):
        self.logger.error(msg)
