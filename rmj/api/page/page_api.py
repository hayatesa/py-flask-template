from jinja2 import TemplateNotFound

from . import page_bp
from flask import render_template


@page_bp.route('/<page_name>.html', methods=['GET'])
def page(page_name):
    try:
        return render_template(page_name + '.html')
    except TemplateNotFound:
        return render_template('404.html')
    except RuntimeError:
        return render_template('404.html')


@page_bp.route('/', methods=['GET'])
def index():
    return render_template('index.html')
