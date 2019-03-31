# -*- coding: utf-8 -*-
from app.entity.user import User
from app.dao.base_dao import BaseDAO


class UserDao(BaseDAO):

    def __init__(self):
        super().__init__(User)

    def find_by_username(self, username):
        return User.query.filter(User.username == username, User.isDeleted == False).all()


user_dao = UserDao()
del UserDao  # 单例模式，删除构函数
