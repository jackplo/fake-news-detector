import os

class Config(object):
    DEBUG = False

    TESTING = False

    CSRF_ENABLED = True

class DevelopmentConfig(Config):
    ENV = "development"
    
    DEVELOPMENT = True
    
    DEBUG = True