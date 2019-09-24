from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from flask_uploads import UploadSet,configure_uploads,IMAGES



app = Flask(__name__)

Login_manager = LoginManager()
Login_manager.session_protection = 'strong'
Login_manager.login_view = 'auth.login'
mail = Mail()
simple = SimpleMDE()
bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)

def create_app(config_name):
    
    app.config.from_object(Config)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint,url_prefix = '/authenticate')

    # from .requests import configure_request
    # configure_request(app)

    bootstrap.init_app(app)
    db.init_app(app)
    Login_manager.init_app(app)
    simple.init_app(app)
    mail.init_app(app)
    configure_uploads(app,photos)

    return app


