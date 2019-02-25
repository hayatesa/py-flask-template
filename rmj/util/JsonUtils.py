import datetime
import json

from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):
    def default(self, obj):

        exclude = []  # exclude fields
        if isinstance(obj.__class__, DeclarativeMeta):
            exclude = ['metadata', 'query', 'query_class']
        fields = {}
        for field in [x for x in dir(obj) if not x.startswith('_') and x not in exclude]:
            data = obj.__getattribute__(field)
            if callable(data):
                continue
            try:
                json.dumps(data, ensure_ascii=False)  # this will fail on non-encodable values, like other classes
                fields[field] = data
            except TypeError:  # 添加了对datetime的处理
                if isinstance(data, datetime.datetime):
                    # fields[field] = data.isoformat()
                    fields[field] = data.strftime('%Y-%m-%d %H:%M:%S')
                elif isinstance(data, datetime.date):
                    fields[field] = data.isoformat()
                elif isinstance(data, datetime.timedelta):
                    fields[field] = (datetime.datetime.min + data).time().isoformat()
                else:
                    fields[field] = None
        # a json-encodable dict
        return fields


def to_json(obj):
    return json.dumps(obj.__dict__, cls=AlchemyEncoder, ensure_ascii=False)
