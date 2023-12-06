from flask import Blueprint
from flask_restful import Api

from ..blueprints import (
    RunTaskTest,
    IsActive,
    GetTask,
    PublicGetMedia,
    AdminGetMedia,
    AdminGetServer,
    AdminPostMedia,
    AdminPostServer,
    AdminUpdateMedia,
    AdminUpdateServer,
    AdminSwitchStatus,
    AdminSimulateLatency,
    GetMediaEndpoint,
    GetAllMedia
)


def init_app(app):
    public_sanity_bp = Blueprint('public_sanity_check', __name__)
    public_sanity_api = Api(public_sanity_bp)
    public_sanity_api.add_resource(IsActive, '/ping')
    app.register_blueprint(public_sanity_bp, url_prefix='/sanity')

    test_endpoint_bp = Blueprint('test_endpoint', __name__)
    test_endpoint_api = Api(test_endpoint_bp)
    test_endpoint_api.add_resource(RunTaskTest, '/testbools:true')
    app.register_blueprint(test_endpoint_bp, url_prefix='/testing')

    polling_endpoint_bp = Blueprint('polling_endpoint', __name__)
    polling_endpoint_api = Api(polling_endpoint_bp)
    polling_endpoint_api.add_resource(GetTask, '/task/<id>')
    app.register_blueprint(polling_endpoint_bp, url_prefix='/poll')

    p_get_media_bp = Blueprint('public_get_media', __name__)
    p_get_media_api = Api(p_get_media_bp)
    p_get_media_api.add_resource(PublicGetMedia, '/<id>')
    app.register_blueprint(p_get_media_bp, url_prefix='/p.get-media')

    a_get_media_bp = Blueprint('admin_get_media', __name__)
    a_get_media_api = Api(a_get_media_bp)
    a_get_media_api.add_resource(AdminGetMedia, '/')
    app.register_blueprint(a_get_media_bp, url_prefix='/a.get-media')

    a_get_server_bp = Blueprint('admin_get_server', __name__)
    a_get_server_api = Api(a_get_server_bp)
    a_get_server_api.add_resource(AdminGetServer, '/')
    app.register_blueprint(a_get_server_bp, url_prefix='/a.get-server')

    a_post_media_bp = Blueprint('admin_post_media', __name__)
    a_post_media_api = Api(a_post_media_bp)
    a_post_media_api.add_resource(AdminPostMedia, '/')
    app.register_blueprint(a_post_media_bp, url_prefix='/a.post-media')

    a_post_server_bp = Blueprint('admin_post_server', __name__)
    a_post_server_api = Api(a_post_server_bp)
    a_post_server_api.add_resource(AdminPostServer, '/')
    app.register_blueprint(a_post_server_bp, url_prefix='/a.post-server')

    a_update_media_bp = Blueprint('admin_update_media', __name__)
    a_update_media_api = Api(a_update_media_bp)
    a_update_media_api.add_resource(AdminUpdateMedia, '/')
    app.register_blueprint(a_update_media_bp, url_prefix='/a.update-media')

    a_update_server_bp = Blueprint('admin_update_server', __name__)
    a_update_server_api = Api(a_update_server_bp)
    a_update_server_api.add_resource(AdminUpdateServer, '/')
    app.register_blueprint(a_update_server_bp, url_prefix='/a.update-server')

    t_switch_server_status_bp = Blueprint('toggle_server_status', __name__)
    t_switch_server_status_api = Api(t_switch_server_status_bp)
    t_switch_server_status_api.add_resource(
        AdminSwitchStatus, '/')
    app.register_blueprint(
        t_switch_server_status_bp, url_prefix='/t.toggle')

    t_simulate_latency_bp = Blueprint('simulate_latency', __name__)
    t_simulate_latency_api = Api(t_simulate_latency_bp)
    t_simulate_latency_api.add_resource(
        AdminSimulateLatency, '/')
    app.register_blueprint(t_simulate_latency_bp, url_prefix='/t.simulate')

    client_get_endpoint_bp = Blueprint('client_get_endpoint', __name__)
    client_get_endpoint_api = Api(client_get_endpoint_bp)
    client_get_endpoint_api.add_resource(
        GetMediaEndpoint, '/')
    app.register_blueprint(client_get_endpoint_bp, url_prefix='/c.get-media')

    client_get_all_endpoint_bp = Blueprint('client_get_all_endpoint', __name__)
    client_get_all_endpoint_api = Api(client_get_all_endpoint_bp)
    client_get_all_endpoint_api.add_resource(
        GetAllMedia, '/')
    app.register_blueprint(client_get_all_endpoint_bp,
                           url_prefix='/c.get-list')
