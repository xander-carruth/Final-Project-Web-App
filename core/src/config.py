from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('ghpcdvZ0CoSXzlisiNzXCMWuelu8rXTRa1Dssqi')
    WTF_CSRF_SECRET_KEY = "testing"
    SESSION_TYPE = 'memcache'

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'

    # Flask-SQLAlchemy
    SQLALCHEMY_DATABASE_URI = 'postgresql://user:password@pg:5432/csc791'
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False