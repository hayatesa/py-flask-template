from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import config

db = SQLAlchemy()


def create_app():
    _app = Flask(__name__)
    _app.config.from_object(config)

    db.init_app(_app)
    CORS(_app, supports_credentials=True, resources={r"/api/*": {"origins": "*"}})

    from rmj.api.demo import demo_bp
    from rmj.api.user import user_bp
    _app.register_blueprint(demo_bp)
    _app.register_blueprint(user_bp)
    return _app


app = create_app()

if __name__ == '__main__':
    app.run()
