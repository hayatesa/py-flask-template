from run import db


class BaseDAO(object):

    def __init__(self, table):
        self.table = table

    def query(self, sql, *params):
        pass
