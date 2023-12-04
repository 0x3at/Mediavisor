from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from celery import Celery


db = SQLAlchemy()

celery = Celery(__name__, broker='redis://localhost')
celery.autodiscover_tasks(['app.celery_tasks'])

def create_app(settings):
    app = Flask(__name__)
    app.config.from_object(settings)
    db.init_app(app)

    from app.api import public_ping_blueprint

    app.register_blueprint(public_ping_blueprint, url_prefix="/isAlive")

    from app.models import Media, Server

    celery.main = app.import_name
    celery.conf.update(app.config)

    with app.app_context():
        db.create_all()
    
    try:
        if settings.UNIT_TEST:
            return app, Media, Server
    except AttributeError:
        pass
        
    return app