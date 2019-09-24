import os


class Config:
    SECRET_KEY = 'happy'
    QUOTE_API_BASE_URL = 'http://quotes.storm.co.uk/random.json'
    QUOTE_API_BASE_URL = os.environ.get('QUOTE_API_BASE_URL')
    MAIL_FIRSTNAME = os.environ.get("MAIL_FIRSTNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    DEBUG = True

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://hapiness:chapati@localhost:5432/blog'
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}

