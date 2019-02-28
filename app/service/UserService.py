from app.entity.User import User
from app.dao.UserDAO import user_dao


def find_list():
    return User.query.all()


def find_page():
    return


def find_by_id(user_id):
    return user_dao.find(user_id)


def find_by_username(username):
    return user_dao.find_by_username(username)
