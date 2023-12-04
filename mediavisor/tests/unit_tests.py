from os import getenv
import random
import time

from dotenv import load_dotenv, find_dotenv

from tests.test_data import movies, servers
from app import create_app

from app.celery_tasks import (
    on_media_upload,
    randomly_simulate_server_latency,
    randomly_switch_server_status,
)

load_dotenv(find_dotenv())


class UnitTestConfiguration:
    SECRET_KEY = getenv("SECRET_KEY")
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = getenv("QA_SQLALCHEMY_DATABASE_URI")
    CELERY_BROKER_URL = getenv("QA_CELERY_BROKER_URL")
    CELERY_RESULT_BACKEND = getenv("QA_CELERY_RESULT_BACKEND")
    UNIT_TEST = True
    broker = getenv("DEVELOPMENT_CELERY_BROKER_URL")
    backend = getenv("DEVELOPMENT_CELERY_RESULT_BACKEND")


def test_get_full_media_list(media_obj):
    success = True
    try:
        media_list = media_obj.get_full_media_list()
        if media_list is None:
            print("DB is empty, or cannot be accessed")
            raise AssertionError

    except Exception as e:
        print(f"Error testing Media.get_full_media_list(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Media.get_full_media_list() was successful: {success} \n-----------"
    )


def test_create_new_media(media_obj):
    success = True
    movie_list = movies

    try:
        for movie in movie_list:
            media_instance = media_obj.create_new_media(
                title=movie["title"],
                description=movie["description"],
                type=movie["type"],
                file_size=movie["file_size"],
                popularity=movie["popularity"],
                returns=True,
            )
            assert media_instance is not None
    except Exception as e:
        success = False
        print(f"Error testing Media.create_new_media(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Media.create_new_media() was successful: {success} \n-----------"
    )


def test_get_media_by_title(media_obj):
    success = True
    movie_list = movies

    try:
        for movie in movie_list:
            media = media_obj.get_media_by_title(title=movie["title"])
            if isinstance(media, list):
                assert movie["description"] == media[0]["description"]
                assert movie["type"] == media[0]["type"]
            elif isinstance(media, dict):
                assert movie["description"] == media["description"]
                assert movie["type"] == media["type"]
            else:
                print(f"Error: {media} is not a list or dict")
                raise AssertionError
    except Exception as e:
        success = False
        print(f"Error: {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Media.get_media_by_title() was successful: {success} \n-----------"
    )


def test_delete_media_by_id(media_obj):
    success = True
    try:
        og_media_list = media_obj.get_full_media_list()
        all_ids = [media["id"] for media in og_media_list]
        random_ids = []

        for num in range(3):
            choice = random.choice(all_ids)
            random_ids.append(choice)
            all_ids.remove(choice)

        for id in random_ids:
            media_obj.delete_media_by_id(id=id)

        new_media_list = media_obj.get_full_media_list()
        assert og_media_list != new_media_list

    except Exception as e:
        print(f"Error testing Media.delete_media_by_id(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Media.delete_media_by_id() was successful: {success} \n-----------"
    )
    print(
        f"-----------\n The following ID's have been deleted: {random_ids} \n-----------"
    )


def test_get_full_server_list(server_obj):
    success = True
    try:
        server_list = server_obj.get_full_server_list()
        print(server_list)
        if server_list is None:
            print("DB is empty, or cannot be accessed")
            raise AssertionError
    except Exception as e:
        print(f"Error testing Server.get_full_server_list(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.get_full_server_list() was successful: {success} \n-----------"
    )


def test_create_new_server(server_obj):
    success = True
    server_list = servers

    try:
        for server in server_list:
            new_server = server_obj.create_new_server(
                endpoint=server["endpoint"],
                is_active=server["is_active"],
                remaining_storage=server["remaining_storage"],
                returns=True,
            )
            assert new_server["id"] is not None
    except Exception as e:
        success = False
        print(f"Error testing Server.create_new_server(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.create_new_server() was successful: {success} \n-----------"
    )


def test_get_server_by_id(server_obj):
    success = True

    try:
        for server in server_obj.get_full_server_list():
            server_result = server_obj.get_server_by_id(id=server["id"])
            assert server["id"] == server_result["id"]

    except Exception as e:
        success = False
        print(f"Error testing Server.get_server_by_id(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.get_server_by_id() was successful: {success} \n-----------"
    )


def test_get_server_by_endpoint(server_obj):
    success = True
    server_list = servers

    try:
        for server in server_list:
            server_result = server_obj.get_server_by_endpoint(
                endpoint=server["endpoint"]
            )
            assert server["endpoint"] == server_result["endpoint"]

    except Exception as e:
        success = False
        print(f"Error testing Server.get_server_by_endpoint(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.get_server_by_endpoint() was successful: {success} \n-----------"
    )


def test_delete_server_by_id(server_obj):
    success = True
    try:
        og_server_list = server_obj.get_full_server_list()
        all_ids = [server["id"] for server in og_server_list]
        choice = random.choice(all_ids)
        server_obj.delete_server_by_id(id=choice)
        new_server_list = server_obj.get_full_server_list()
        assert og_server_list != new_server_list
    except Exception as e:
        print(f"Error testing Server.delete_server_by_id(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.delete_server_by_id() was successful: {success} \n-----------"
    )
    print(f"-----------\n The following ID has been deleted: {choice} \n-----------")


def test_delete_server_by_endpoint(server_obj):
    success = True
    try:
        og_server_list = server_obj.get_full_server_list()
        all_endpoints = [server["endpoint"] for server in og_server_list]
        choice = random.choice(all_endpoints)
        server_obj.delete_server_by_id(endpoint=choice)
        new_server_list = server_obj.get_full_server_list()
        assert og_server_list != new_server_list
    except Exception as e:
        print(f"Error testing Server.delete_server_by_id(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.delete_server_by_id() was successful: {success} \n-----------"
    )
    print(f"-----------\n The following ID has been deleted: {choice} \n-----------")


def test_switch_server_status(server_obj):
    success = True
    try:
        og_server_list = server_obj.get_full_server_list()
        all_ids = [server["id"] for server in og_server_list]
        choice = random.choice(all_ids)
        server_instance = server_obj.retrieve_server_instance(id=choice)
        og_status = server_obj.get_server_by_id(id=choice)["is_active"]

        server_instance.switch_server_status()
        new_status = server_obj.get_server_by_id(id=choice)["is_active"]
        assert og_status != new_status
        assert new_status == server_instance.is_active
    except Exception as e:
        print(f"Error testing Server.switch_server_status(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of Server.switch_server_status() was successful: {success} \n-----------"
    )
    print(f"-----------\n The following ID has been switched: {choice} \n-----------")


def test_randomly_switch_server_status(server_obj):
    success = True
    try:
        og_server_list = server_obj.get_full_server_list()
        randomly_switch_server_status.delay()
        time.sleep(10)
        new_server_list = server_obj.get_full_server_list()
        changed_servers = []
        for og_server in og_server_list:
            for new_server in new_server_list:
                if (
                    og_server["id"] == new_server["id"]
                    and og_server["is_active"] != new_server["is_active"]
                ):
                    new_server_list.remove(new_server)
                    changed_servers.append(new_server)
    except Exception as e:
        print(f"Error testing randomly_switch_server_status(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of randomly_switch_server_status() was successful: {success} \n-----------"
    )
    print(
        f"-----------\n The following ID's have been switched: {[server['id'] for server in changed_servers]} \n-----------"
    )


def test_on_media_upload_task(media_obj):
    success = True
    try:
        updated_servers = []
        for media in media_obj.get_full_media_list():
            if media_obj.get_media_by_id(id=media["id"])["server_list"] == []:
                on_media_upload.delay(media)
                
                updated_servers.append(media["id"])
    except Exception as e:
        print(f"Error testing on_media_upload(): {e}")
        raise AssertionError
    print(
        f"-----------\n Testing of on_media_upload() was successful: {success} \n-----------"
    )
    print(
        f"-----------\n The following ID's have been updated: {updated_servers} \n-----------"
    )


if __name__ == "__main__":
    app, media, server = create_app(UnitTestConfiguration)
    app_context = app.app_context()
    app_context.push()
    try:
        test_create_new_media(media)
        test_create_new_server(server)
        test_on_media_upload_task(media)
        test_randomly_switch_server_status(server)
    except Exception as e:
        print(f"Error: {e}")
        raise AssertionError
    app_context.pop()
