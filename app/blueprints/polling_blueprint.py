from flask import jsonify
from flask_restful import Resource


class GetTask(Resource):
    def get(self, id):
        from .. import celery
        task = celery.AsyncResult(id)
        task_id = task.id
        task_state = task.state
        task_result = task.result
        traceback = task.traceback

        response_data = {
            'data': None,
            'status_code': None,
            'task_id': task_id,
            'state': task_state,
            'traceback': traceback
        }

        if task_state == 'PENDING':
            response_data['status_code'] = 200
            response_data['data'] = 'Task is Pending!'
        elif task_state == 'FAILURE':
            response_data['status_code'] = 500
            response_data['data'] = 'Task has failed!'
        elif task_state == 'SUCCESS':
            response_data['status_code'] = 200
            response_data['data'] = task_result
        else:
            response_data['status_code'] = 400
            response_data['data'] = 'Unknown task state'

        response = jsonify(response_data)
        response.status_code = response_data['status_code']
        return response
