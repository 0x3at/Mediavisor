from app import create_app, celery
from ..interfaces import TestInterface, MediaInterface, ServerInterface
from time import sleep
import random


test_interface = TestInterface()
media_interface = MediaInterface()
server_interface = ServerInterface()


def simulate_server_latency():
    base_latency = random.uniform(1, 20)
    congestion_factor = random.uniform(0.8, 1.2)
    load_factor = random.uniform(0.8, 1.2)
    bandwidth_factor = random.uniform(0.8, 1.2)

    latency = (
        base_latency * congestion_factor * load_factor * bandwidth_factor
    )

    jitter = random.uniform(0, 5)
    latency += jitter

    return latency


def dynamically_select_servers(media_obj, servers):
    media = media_obj.to_dict()
    popularity = media["popularity"]
    servers.sort(key=lambda server: (
        server["latency"], -server["remaining_storage"]))

    server_count = calculate_server_count(servers, popularity)

    selected_servers = servers[:server_count]

    return selected_servers


def calculate_server_count(available_servers, popularity):
    if popularity > 9:
        base_count = 5
    elif popularity > 8:
        base_count = 4
    elif popularity > 6:
        base_count = 3
    else:
        base_count = 2

    scaled_count = base_count + popularity

    return min(scaled_count, len(available_servers))


def on_media_upload(media):
    server_list = server_interface.get_full_list()
    available_servers = [
        server for server in server_list if server['is_active']]
    selected_servers = dynamically_select_servers(
        media, available_servers)
    for server in selected_servers:
        server_interface.add_media_to_relational_mapping(
            media, server)
        server_instance = server_interface.retrieve_server_instance(
            server['id'])
        media_interface.add_server_to_relational_mapping(
            media, server_instance)
    return {
        "media_id": media.id,
        'servers': media_interface.get_server_ids_for_media(media)
    }


@celery.task
def get_media(media_identifier, public=True):
    app = create_app('qa')
    with app.app_context():
        if public:
            if type(media_identifier) == str:
                media = media_interface.get_media_by_title(media_identifier)
        if not public:
            if type(media_identifier) == str:
                media = media_interface.get_media_by_title(media_identifier)
            if type(media_identifier) == int:
                media = media_interface.get_media_by_id(media_identifier)
    return media


@celery.task
def update_media(id, values):
    app = create_app('qa')
    with app.app_context():
        clean_values = {key: value for key,
                        value in values.items() if value != ""}
        media = media_interface.update_media_by_id(
            id, clean_values, returns=True)
    return media


@celery.task
def get_server(server_identifier):
    app = create_app('qa')
    with app.app_context():
        if type(server_identifier) == str:
            server = server_interface.get_server_by_endpoint(server_identifier)

        if type(server_identifier) == int:
            server = server_interface.get_server_by_id(server_identifier)
    return server


@celery.task
def update_server(id, values):
    app = create_app('qa')
    with app.app_context():
        clean_values = {key: value for key,
                        value in values.items() if value != ""}
        server = server_interface.update_server_by_id(
            id, clean_values, returns=True)
    return server


@celery.task
def test_bool_true():
    app = create_app('qa')
    test_data = None
    with app.app_context():
        for _ in range(1, 10):
            test_data = test_interface.add_data_to_table(returns=True)
    return test_data


@celery.task
def upload_media(media_attributes):
    app = create_app('qa')
    with app.app_context():
        new_media = media_interface.create_new_media(
            media_attributes, returns=[True, 'instance'])
        on_media_upload(new_media)
        return new_media.to_dict()


@celery.task
def upload_server(server_attributes):
    app = create_app('qa')
    with app.app_context():
        new_server = server_interface.create_new_server(
            server_attributes, returns=True)
    return new_server


def switch_all_server_status_randomly():
    app = create_app('qa')
    with app.app_context():
        server_list = server_interface.get_full_list()
        for server in server_list:
            is_switched = random.choice([True, False, False])
            if is_switched:
                server_interface.switch_server_status(server['id'])


def simulate_server_latency_randomly():
    app = create_app('qa')
    with app.app_context():
        server_list = server_interface.get_full_list()
        for server in server_list:
            latency = simulate_server_latency()
            server_interface.update_server_by_id(server['id'],
                                                 {'latency': latency})


@celery.task
def get_all_media():
    app = create_app('qa')
    with app.app_context():
        media_list = media_interface.get_full_list()
    return media_list


@celery.task
def retrieve_best_server_for_media(media_id):
    app = create_app('qa')
    with app.app_context():
        simulate_server_latency_randomly()
        switch_all_server_status_randomly()
        media = media_interface.get_media_by_id(media_id)
        servers = media["server_list"]
        active_servers = []
        for server_id in servers:
            server = server_interface.get_server_by_id(server_id)
            if server['is_active']:
                active_servers.append(server)

        sorted_servers = sorted(active_servers, key=lambda server: (
            server["latency"]))

        return sorted_servers[0]
