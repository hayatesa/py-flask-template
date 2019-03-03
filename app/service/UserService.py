from app.entity.User import User
from app.dao.UserDAO import user_dao
from . import session_commit


class UserService:

    @staticmethod
    def find_list():
        return User.query.all()

    @staticmethod
    def find_page(self):
        return

    @staticmethod
    def find_by_id(user_id):
        return user_dao.find(user_id)

    @staticmethod
    def find_by_username(username):
        users = user_dao.find_by_username(username)
        if not users:
            return None
        return users[0]

    @staticmethod
    def update(user):
        user_dao.update(user)
        session_commit()


user_service = UserService()
