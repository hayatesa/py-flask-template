from app.entity.User import User
from .BaseDAO import BaseDAO


class UserDAO(BaseDAO):

    def __init__(self):
        super().__init__(User)

    def find_by_username(self, username):
        return User.query.filter(User.username.like(r'%{}%'.format(username))).all()


user_dao = UserDAO()
