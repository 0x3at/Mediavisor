from flask import jsonify
from flask_restful import Resource, reqparse

get_media_parser = reqparse.RequestParser()
get_media_parser.add_argument('id', type=int, required=True, location='json')


class GetMediaEndpoint(Resource):
    def get(self):
        from ..celery_tasks import retrieve_best_server_for_media
        args = get_media_parser.parse_args()
        task = retrieve_best_server_for_media.delay(args['id'])
        status_code = 202
        response = jsonify({
            'status_code': status_code,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class GetAllMedia(Resource):
    def get(self):
        from ..celery_tasks import get_all_media
        task = get_all_media.delay()
        status_code = 202
        response = jsonify({
            'status_code': status_code,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response
