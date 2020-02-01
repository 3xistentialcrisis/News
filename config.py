import os

class Config():
    '''
    Main Config Class
    '''
    
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    # NEWS_API_BASE_URL =

class ProdConfig(Config):
    '''
    App Production child configuration class
    '''
    pass


class DevConfig(Config):
    '''
    App Development child configuration class
    '''
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}