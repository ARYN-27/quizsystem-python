import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY = os.environ.get('BAEK4CuxCzrrxwEE') or 'BAEK4CuxCzrrxwEE'
    SQLALCHEMY_DATABASE_URI = os.environ.get('sqlite:///db.sqlite') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False