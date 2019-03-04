from app.mixin.ConvertMixin import ConvertMixin


class UserVO(object, ConvertMixin):

    def __init__(self, id, username, last_access_time):
        self.id = id
        self.username = username
        self.lassAccessTime = last_access_time

    @staticmethod
    def convert(source):
        return UserVO(source.id, source.username, source.lastAccessTime)
