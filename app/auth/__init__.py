from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


login_manager =LoginManager()
login_manager.session_protection='strong'
login_manager.login_view='auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)
