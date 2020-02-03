import os

class Config():
    '''
    Main Config Class
    '''
    
    NEWS_API_KEY = '3540aa7416f144918cf919d37f574a5c'
    # NEWS_API_KEY = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources/' 

    # NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')

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