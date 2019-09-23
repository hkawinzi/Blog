from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet,configure_uploads,IMAGES

Login_manager = LoginManager()
Login_manager.session_protection = 'strong'
Login_manager.login_view = 'auth.login'
mail = Mail()
simple = SimpleMDE()
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_options[config_name])
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

