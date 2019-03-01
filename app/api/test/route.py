from app.entity.User import User
from flask_restplus import Resource, fields, Namespace

ns = Namespace("test", description="Test CURD api.")

test_model = ns.model('TestModel', {
    'id': fields.String(readOnly=True, description='The id'),
    'username': fields.String(required=True, description='The username'),
})
test_list_model = ns.model('TestListModel', {
    'users': fields.List(fields.Nested(test_model)),
    'total': fields.Integer,
})


@ns.route("")
class Test(Resource):
    # 初始化数据
    users = [User(), User()]

    @ns.doc('get_list')
    @ns.marshal_with(test_list_model)
    def get(self):
        return {
            "users": self.users,
            "total": len(self.users),
        }

    @ns.doc('')
    @ns.expect(test_model)
    @ns.marshal_with(test_model, code=201)
    def post(self):
        user = User()
        return user

    @ns.doc('')
    @ns.expect(test_model)
    @ns.marshal_with(test_model, code=201)
    def put(self):
        user = User()
        return user

    @ns.doc('')
    @ns.expect(test_model)
    @ns.marshal_with(test_model, code=201)
    def delete(self):
        user = User()
        return user

    @ns.doc('/<user_id>')
    @ns.marshal_with(test_model)
    def delete(self, id):
        user = User()
        user.id = id
        return user
