# # from rmj.entity.Base import Base
# import uuid
# from app import db
# from .Base import Base
#
#
# class DemoEntity1(Base):
#     __tablename__ = 'demo_entity'
#
#     id = db.Column(db.String(32), primary_key=True)
#
#     create_by = db.Column(db.String(64), primary_key=False)
#
#     gmt_created = db.Column(db.DateTime, primary_key=False)
#
#     gmt_modified = db.Column(db.DateTime, primary_key=False)
#
#     is_deleted = db.Column(db.DateTime, primary_key=False)
#
#     remarks = db.Column(db.String(255), primary_key=False)
#
#     update_by = db.Column(db.String(64), primary_key=False)
#     version = db.Column(db.Integer, primary_key=False)
#
#     d_name = db.Column(db.String, primary_key=False)
#
#     def __init__(self, id, create_by, ):
#         self.id = uuid.uuid1()
#         self.name = name
#
#     def __repr__(self):
#         return '<Demo1 %r>' % self.name
