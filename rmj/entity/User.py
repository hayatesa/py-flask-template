from run import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.String(32), primary_key=True)
    username = db.Column(db.String(255))
    create_time = db.Column(db.DateTime)

    def __init__(self):
        super(User, self).__init__()

    def __repr__(self):
        return self.username
