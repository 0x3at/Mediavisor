import json

from flask_restful import Resource, abort

from app.celery_tasks import on_media_upload


class IsActiveEndpoint(Resource):
    def get(self):
        on_media_upload.delay({"id":1})
        return {"message": "Server is up and running!"}, 200
