from . import user_api
from app.entity.User import User
from app.util.Resp import mk_resp
from app import logger
from app.service import UserService
from flask_restplus import Resource, fields, Namespace

ns = Namespace("users", description="Users CURD api.")

user_model = ns.model('UserModel', {
    'user_id': fields.String(readOnly=True, description='The user unique identifier'),
    'username': fields.String(required=True, description='The user nickname'),
})
user_list_model = ns.model('UserListModel', {
    'users': fields.List(fields.Nested(user_model)),
    'total': fields.Integer,
})



# @ns.doc('/')
# @ns.marshal_with(user_list_model)
# def get(self):
#     logger.info('List users.')
#     return mk_resp(data=User.query.all())
#
# @ns.doc('/<user_id>')
# @ns.marshal_with(user_list_model)
# def get(self, user_id):
#     logger.info('Find users by id: %s.' % user_id)
#     return mk_resp(data=UserService.find_by_id(user_id))
#
# @ns.doc('/username/<username>')
# @ns.marshal_with(user_list_model)
# def get(self, username):
#     logger.info('Find users by username: %s.' % username)
#     return mk_resp(data=UserService.find_by_username(username))




