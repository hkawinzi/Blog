import os

class Config:
    QUOTE_API_BASE_URL = 'http://quotes.storm.co.uk/random.json'
    QUOTE_API_BASE_URL = os.environ.get('QUOTE_API_BASE_URL')
    MAIL_FIRSTNAME = os.environ.get("MAIL_FIRSTNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    UPLOADED_PHOTOS_DEST = 'app/static/photos'