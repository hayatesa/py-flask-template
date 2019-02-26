from ..entity.User import User
from .BaseDAO import BaseDAO


class UserDAO(BaseDAO):

    def __init__(self):
        super().__init__(User)
