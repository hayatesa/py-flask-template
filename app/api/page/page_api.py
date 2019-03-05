from jinja2 import TemplateNotFound
from flask import send_file
from . import page_bp as api


@api.route('/<page_name>.html', methods=['GET'])
def page(page_name):
    try:
        return send(page_name + '.html')
    except TemplateNotFound:
        return send('404.html')
    except RuntimeError:
        return send('404.html')


@api.route('/', methods=['GET'])
def index():
    return send('index.html')


def send(file):
    from app import app
    return send_file(app.static_folder + '/' + file)
