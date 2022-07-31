import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
configdir = os.environ.get('CONFIG_DIR') or '/home/ryanm/code/flask-react-login/backend/config'
load_dotenv(os.path.join(configdir, '.env'), verbose=True)


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    REMEMBER_COOKIE_NAME = os.environ.get('SECRET_KEY') or 'SESS_REM_ME'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(configdir, 'sqlite.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Development configurations
    """
    DEBUG = True
    SQLALCHEMY_ECHO = True
    TEMPLATES_AUTO_RELOAD = True


class ProductionConfig(Config):
    """
    Production configurations
    """
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
