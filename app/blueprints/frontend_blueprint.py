from flask import Blueprint, render_template, redirect, request, url_for, jsonify


frontend_blueprint = Blueprint('frontend', __name__)


@frontend_blueprint.route('/')
def index():
    return render_template('base.html')


@frontend_blueprint.route('/home/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        from ..celery_tasks import get_all_media
        media_list = get_all_media()
        current_url = request.url
        return render_template('media.html', objects=media_list, current_url=current_url)

    if request.method == 'POST':
        from ..celery_tasks import retrieve_best_server_for_media
        # Extract the ID from the request data
        media_id = request.form.get('id')
        task = retrieve_best_server_for_media.delay(media_id)
        status_code = 202
        response = jsonify({
            'status_code': status_code,
            'task_id': task.id,
            'task_status:': f'Task is now {task.state}',
            'endpoint': f'http://localhost:5000/poll/task/{task.id}'})
        response.status_code = status_code
        return response
