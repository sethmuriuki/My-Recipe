import os

class Config:
    '''
    General configurations parent class
    '''

    RECIPE_BASE_URL = "http://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"
    SECRET_KEY = 'SECRET_KEY'


class ProdConfig(Config):
    pass



class DevConfig(Config):

   DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
