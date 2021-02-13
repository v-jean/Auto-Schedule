from flask_sqlalchemy import SQLAlchemy
from config import config_dict
from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"

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

    #url_prefix add /auth before route name
    from .auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/auth")

    #
    login_manager.init_app(app)

    return app