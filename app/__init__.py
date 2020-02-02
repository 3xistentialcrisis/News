from flask import Flask
from flask_bootstrap import Bootstrap 
from config import config_options

#Create Bootstrap Instance
bootstrap = Bootstrap()

#create_app Function
def create_app(config_name):

    app = Flask(__name__)

    #Creating application configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    return app