from uuid import uuid1


class BaseDAO:

    def __init__(self, mapper):
        self.__mapper = mapper

    def find(self, id):
        mapper = self.__mapper
        return mapper.query.filter(mapper.isDeleted != 1, mapper.id == id).all()

    def delete(self, id):
        mapper = self.__mapper
        mapper.query.filter(mapper.isDeleted == 0, mapper.id == id).delete()

    def add(self, obj):
        obj.id = uuid1()
        self.__mapper.query.add(obj)

    def update(self, obj):
        mapper = self.__mapper
        mapper.query.filter_by(mapper.id == obj.id).update(obj)
