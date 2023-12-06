# import json
from flask import jsonify
from flask_restful import Resource


class RunTaskTest(Resource):
    def get(self):
        from ..celery_tasks import test_bool_true

        task = test_bool_true.delay()
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = 202
        return response


class IsActive(Resource):
    def get(self):
        response = jsonify({
            'data': 'Hello, World!',
            'status_code': 200})
        response.status_code = 200
        return response


class PublicGetMedia(Resource):
    def get(self, id):
        from ..celery_tasks import get_media
        task = get_media.delay(id)
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = response['status_code']
        return response
