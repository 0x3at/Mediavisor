from flask import Flask
from app.ext import database
from app.ext import blueprint
from app.ext import config
from app.ext import celeryext

db = database.DB
celery = celeryext.CELERY


def create_app(env):
    """
    configs = {
        "dev": DevelopmentConfiguration,
        "qa": QAConfiguration,
    }   
    """
    app = Flask(__name__)
    config.init_app(app, env)
    database.init_app(app)
    blueprint.init_app(app)
    celeryext.init_app(app)

    return app
