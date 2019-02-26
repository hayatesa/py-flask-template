from app import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column('id', db.String(32), primary_key=True)
    username = db.Column('username', db.String(255))
    createTime = db.Column('create_time', db.DateTime)

    def __init__(self):
        super(User, self).__init__()

    def __repr__(self):
        return self.username
