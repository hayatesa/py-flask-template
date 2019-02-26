from app import DB


class BaseDAO(object):

    def __init__(self, table):
        self.table = table

    def query(self, sql, *params):
        pass
