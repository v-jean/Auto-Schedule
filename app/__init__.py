from flask_sqlalchemy import SQLAlchemy
from config import config_dict
from flask import Flask

db = SQLAlchemy()

#to create flask app and db in manage.py
def appFactory(option):
    app = Flask(__name__)
    app.config.from_object(config_dict[option])
    app.template_folder = "html"
    db.init_app(app)

    #pass defined blueprint to flask app
    from .main import main_bp
    app.register_blueprint(main_bp)

    return app