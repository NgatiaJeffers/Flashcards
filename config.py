import os

class Config:
    '''
    General configuration parent class
    '''

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa-access:Access@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    '''
    Production configuration child class

    Args:
        Config: The parent configuration class with general configuration settings
    '''


class DevConfig(Config):
    '''
    Development configuration child class

    Args:
        Config: The parent configuration class with General configuaration settings
    '''

class TestConfig(Config):
    '''
    Testing Configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}