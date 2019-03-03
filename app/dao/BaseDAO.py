from uuid import uuid1
from sqlalchemy.exc import SQLAlchemyError

from app import db


class BaseDAO:

    def __init__(self, mapper):
        self.__mapper = mapper

    def find(self, id):
        mapper = self.__mapper
        return mapper.query.filter(mapper.isDeleted == 0, mapper.id == id).all()

    def delete(self, id):
        db.session.delete(self.find(id))

    def add(self, obj):
        obj.id = uuid1()
        db.session.add(obj)

    def update(self, obj):
        db.session.add(obj)
