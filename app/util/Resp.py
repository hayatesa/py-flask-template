from app.util.JsonUtils import to_json
from datetime import datetime
from flask import Response


class Resp:

    def __init__(self, success, message, data):
        self.success = success
        self.message = message
        self.timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.data = data

    def to_json(self):
        return to_json(self)


def mk_resp(success=True, message='', data=None):
    return Response(Resp(success, message, data).to_json(), mimetype='application/json;charset=utf-8')
