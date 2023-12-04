from os import getenv

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Configuration:
    DEBUG = False
    SECRET_KEY = getenv("SECRET_KEY")


class DevelopmentConfiguration(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv("DEVELOPMENT_SQLALCHEMY_DATABASE_URI")
    broker = getenv("DEVELOPMENT_CELERY_BROKER_URL")
    backend = getenv("DEVELOPMENT_CELERY_RESULT_BACKEND")


class QAConfiguration(Configuration):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv("QA_SQLALCHEMY_DATABASE_URI")
    CELERY_BROKER_URL = getenv("QA_CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = getenv("QA_CELERY_RESULT_BACKEND")
