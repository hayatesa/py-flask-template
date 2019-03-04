from flask_restplus import Namespace, Resource
from app.util.Resp import success
from app import logger
from app.service.UserService import user_service

user_api = Namespace('user', description='Token API')


@user_api.route('/list')
class UserApi(Resource):
    def get(self):
        logger.info('List users.')
        return success(data=user_service.find_list())


@user_api.route('/<string:id>')
@user_api.param('id', 'The task identifier')
class UserApi(Resource):
    def get(self, id):
        logger.info('List users.')
        return success(data=user_service.find_by_id(id))

    def post(self, id):
        logger.info('Add user.')
        return success(data=user_service.add(id))

    def delete(self, id):
        logger.info('Delete user.')
        user_service.delete(id)
        return success()


@user_api.route('/<string:username>')
class UserApi(Resource):
    def get(self, username):
        logger.info('List users.')
        return success(data=user_service.find_by_username(username))
