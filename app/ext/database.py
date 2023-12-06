from flask_sqlalchemy import SQLAlchemy


_db = SQLAlchemy()
DB = _db


def init_app(app):
    DB.init_app(app)
    from ..models import Media, Server

    with app.app_context():
        DB.create_all()

    return DB
