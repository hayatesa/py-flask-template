from ..entity import DemoEntity1


def find_by_id():
    return DemoEntity1.query.filter_by(id='17d79f4e667a11e895ff0050569c7697')
