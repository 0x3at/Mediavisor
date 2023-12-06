from celery import Celery
from celery.result import AsyncResult


_celery = Celery(__name__, broker='redis://localhost:6379/0',
                 backend='redis://localhost:6379/0')
_celery.autodiscover_tasks(['app.celery_tasks'])
CELERY = _celery


def init_app(app):
    CELERY.main = app.import_name

    return CELERY
