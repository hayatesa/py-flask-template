class UserVO:

    def __init__(self, id, username, reg_time):
        self.id = id
        self.username = username
        self.regTime = reg_time

    @staticmethod
    def convert(source, target):
        return dict()
