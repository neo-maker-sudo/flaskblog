import os
import pathlib

class Config:
    # python bulid in secrets-module : secrets
    SECRET_KEY = os.environ.get('SECRET_KEY_FLASKBLOG')
    # database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(pathlib.Path(__file__).parent, 'site.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #email
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
    
