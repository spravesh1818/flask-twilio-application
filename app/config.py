import os

basedir = os.path.abspath(os.path.dirname(__file__))


class DefaultConfig(object):
    SECRET_KEY = 'secret-key'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TWILIO_ACCOUNT_SID ='AC1c335cc56649c8f22cf79b94cddaf067'
    TWILIO_AUTH_TOKEN ='0c304dadbdc73d17f09a2ad4da94e132'
    TWILIO_NUMBER = '+14805264941'
    TWIML_APPLICATION_SID ="AP50da95622c320f6c7e02c53d307088f4"
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