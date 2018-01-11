import os

class Config:
    '''
    General configurations parent class
    '''

    RECIPE_BASE_URL = "http://www.themealdb.com/api/json/v1/1/lookup.php?i=52772"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY ='one'

class ProdConfig(Config):

   SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')



class DevConfig(Config):

   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://seth:seth@localhost/recipe'

   DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig
}
