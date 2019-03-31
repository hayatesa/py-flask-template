# -*- coding: utf-8 -*-
from app.api import token_auth
from app.util import sys_util
from app.api import version
from app.util.resp import success
from app.api.sys import sys_bp as api


@api.route('sys-info')
@token_auth.login_required
def get():
    info = {
        'version': version,
        'os': sys_util.get_platform(),
        'machine': sys_util.get_machine(),
        'processor': sys_util.get_processor(),
        'python version': sys_util.get_python_version()

    }
    return success(data=info)
