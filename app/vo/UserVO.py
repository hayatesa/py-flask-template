from app.mixin.ConvertMixin import ConvertMixin


class UserVO(ConvertMixin):

    def __init__(self, id, username, last_access_time):
        self.id = id
        self.username = username
        self.lastAccessTime = last_access_time

    @staticmethod
    def convert(source):
        return UserVO(source.id, source.username, source.lastAccessTime)
