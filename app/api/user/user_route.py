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


@ns.route("users")
class UserListApi(Resource):
    # 初始化数据
    users = [User(), User()]

    @ns.doc('get_user_list')
    @ns.marshal_with(user_list_model)
    def get(self):
        return {
            "users": self.users,
            "total": len(self.users),
        }

    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        user = User()
        return user

# @ns.route('/', methods=['GET'])
# def find_list():
#     logger.info('List users.')
#     return mk_resp(data=User.query.all())
#
#
# @ns.route('/<user_id>', methods=['GET'])
# def find_by_id(user_id):
#     logger.info('Find users by id: %s.' % user_id)
#     return mk_resp(data=UserService.find_by_id(user_id))
#
#
# @ns.route('username/<username>', methods=['GET'])
# def find_by_name(username):
#     logger.info('Find users by username: %s.' % username)
#     return mk_resp(data=UserService.find_by_username(username))
