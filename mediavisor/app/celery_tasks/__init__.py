import random

from app import celery, create_app
from app.models import Media, Server
from app.utils import simulate_server_latency

Media = Media()

def dynamically_select_servers(media, servers):
    popularity = media["popularity"]
    servers.sort(key=lambda server: (server["latency"], -server["remaining_storage"]))

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


@celery.task
def on_media_upload(media):
    media_instance = Media.retrieve_media_instance(media["id"])
    server_list = Server.get_full_server_list()
    available_servers = [
        server
        for server in server_list
        if server["is_active"] and server["remaining_storage"] > media["file_size"]
    ]
    selected_servers = dynamically_select_servers(media, available_servers)
    for server in selected_servers:
        server_instance = Server.retrieve_server_instance(server["id"])
        server_instance.remaining_storage -= media["file_size"]
        if (
            media_instance not in server_instance.media_ids
            and server_instance not in media_instance.server_list
        ):
            server_instance.media_ids.append(media_instance)
            media_instance.server_list.append(server_instance)
    print("worker complete :\n ",media_instance.server_list)


@celery.task
def randomly_simulate_server_latency():
    server_list = Server.get_full_server_list()
    for server in server_list:
        server_instance = Server.retrieve_server_instance(server["id"])
        latency_simulation = simulate_server_latency()
        server_instance.latency = latency_simulation
        Server.update_server_by_id(
            id=server_instance.id, values=[{"latency": latency_simulation}]
        )


@celery.task
def randomly_switch_server_status():
    server_list = Server.get_full_server_list()

    for server in server_list:
        choice = random.choice([True, False, "filler", "filler"])
        if choice == True:
            server_instance = Server.retrieve_server_instance(server["id"])
            server_instance.switch_server_status()
            Server.update_server_by_id(
                id=server_instance.id, values=[{"is_active": server_instance.is_active}]
            )
