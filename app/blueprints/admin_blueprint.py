from flask import jsonify
from flask_restful import Resource, reqparse


post_media_parser = reqparse.RequestParser()
post_media_parser.add_argument(
    'title', type=str, required=True, location='json')
post_media_parser.add_argument(
    'description', type=str, required=True, location='json')
post_media_parser.add_argument(
    'type', type=str, required=True, location='json')
post_media_parser.add_argument(
    'file_size', type=int, required=True, location='json')
post_media_parser.add_argument(
    'popularity', type=int, required=True, location='json')

post_server_parser = reqparse.RequestParser()
post_server_parser.add_argument(
    'endpoint', type=str, required=True, location='json')
post_server_parser.add_argument(
    'is_active', type=bool, required=True, location='json')
post_server_parser.add_argument(
    'remaining_storage', type=int, required=True, location='json')


get_media_parser = reqparse.RequestParser()
get_media_parser.add_argument('id', type=int, required=True, location='json')

get_server_parser = reqparse.RequestParser()
get_server_parser.add_argument('identifier', required=True, location='json')

put_media_parser = reqparse.RequestParser()
put_media_parser.add_argument('id', type=int, required=True, location='json')
put_media_parser.add_argument(
    'title', type=str, required=False, location='json')
put_media_parser.add_argument(
    'description', type=str, required=False, location='json')
put_media_parser.add_argument(
    'type', type=str, required=False, location='json')
put_media_parser.add_argument(
    'file_size', type=int, required=False, location='json')
put_media_parser.add_argument(
    'popularity', type=int, required=False, location='json')

put_server_parser = reqparse.RequestParser()
put_server_parser.add_argument('id', type=int, required=True)
put_server_parser.add_argument(
    'endpoint', type=str, required=False, location='json')
put_server_parser.add_argument(
    'is_active', type=bool, required=False, location='json')
put_server_parser.add_argument(
    'remaining_storage', type=int, required=False, location='json')
put_server_parser.add_argument(
    'latency', type=int, required=False, location='json')


class AdminPostMedia(Resource):
    def post(self):
        from ..celery_tasks import upload_media
        args = post_media_parser.parse_args()
        task = upload_media.delay(args)
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminPostServer(Resource):
    def post(self):
        from ..celery_tasks import upload_server
        args = post_server_parser.parse_args()
        task = upload_server.delay(args)
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminGetMedia(Resource):
    def get(self):
        from ..celery_tasks import get_media
        args = get_media_parser.parse_args()
        task = get_media.delay(int(args['id']), public=False)
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminGetServer(Resource):
    def get(self):
        from ..celery_tasks import get_server
        args = get_server_parser.parse_args()
        task = get_server.delay(args['identifier'])
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminUpdateMedia(Resource):
    def put(self):
        from ..celery_tasks import update_media
        args = put_media_parser.parse_args()
        task = update_media.delay(args['id'], args)
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminUpdateServer(Resource):
    def put(self):
        from ..celery_tasks import update_server
        args = put_server_parser.parse_args()
        task = update_server.delay(args['id'], args)
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminSwitchStatus(Resource):
    def get(self):
        from ..celery_tasks import switch_all_server_status_randomly
        task = switch_all_server_status_randomly.delay()
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response


class AdminSimulateLatency(Resource):
    def get(self):
        from ..celery_tasks import simulate_server_latency_randomly
        task = simulate_server_latency_randomly.delay()
        status_code = 202
        response = jsonify({
            'status_code': 202,
            'task_id': task.id,
            'task_status:': f'Task is now {task.status}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response
