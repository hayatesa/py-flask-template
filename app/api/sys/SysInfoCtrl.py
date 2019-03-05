from flask_restplus import Resource, Namespace

from app.security import token_auth
from app.util import SysUtils
from app.api import version
from app.util.Resp import success

sys_api = Namespace('info')


@sys_api.route('')
class SysInfoCtrl(Resource):

    @token_auth.login_required
    @sys_api.doc(security='bearerAuth')
    def get(self):
        info = {
            'version': version,
            'os': SysUtils.get_platform(),
            'machine': SysUtils.get_machine(),
            'processor': SysUtils.get_processor(),
            'python version': SysUtils.get_python_version()

        }
        return success(data=info)
