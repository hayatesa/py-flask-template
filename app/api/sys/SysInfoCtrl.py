from app.security import token_auth
from app.util import SysUtils
from app.api import version
from app.util.Resp import success
from . import sys_bp as api


@api.route('sys-info')
@token_auth.login_required
def get():
    info = {
        'version': version,
        'os': SysUtils.get_platform(),
        'machine': SysUtils.get_machine(),
        'processor': SysUtils.get_processor(),
        'python version': SysUtils.get_python_version()

    }
    return success(data=info)
