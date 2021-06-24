import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TWILIO_ACCOUNT_SID =''
    TWILIO_AUTH_TOKEN =''
    TWILIO_NUMBER = '+17027102665'
    TWIML_APPLICATION_SID ="AP16b7b56fd0b1b1e374381bd7bc1124e1"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID', None)
    # TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN', None)
    # TWILIO_NUMBER = os.environ.get('TWILIO_NUMBER', None)
    # TWIML_APPLICATION_SID = os.environ.get('TWIML_APPLICATION_SID', None)


class DevelopmentConfig(DefaultConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'dev.sqlite')


class TestConfig(DefaultConfig):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    DEBUG = True

config_env_files = {
    'test': 'browser_calls_flask.config.TestConfig',
    'development': 'browser_calls_flask.config.DevelopmentConfig',
}