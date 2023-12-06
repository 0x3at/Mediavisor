import requests
from time import sleep, time
import json


import threading

endpoint = {
    'sanity': 'http://localhost:5000/sanity/ping',
    'test_tasks': 'http://localhost:5000/testing/testbools:true',
    'poll': 'http://localhost:5000/poll/task/',
    'get-media': 'http://localhost:5000/p.get-media/',
    'get-media': 'http://localhost:5000/a.get-media/',
    'get-server': 'http://localhost:5000/a.get-server/',
    'post-media': 'http://localhost:5000/a.post-media/',
    'post-server': 'http://localhost:5000/a.post-server/',
    'update-media': 'http://localhost:5000/a.update-media/',
    'update-server': 'http://localhost:5000/a.update-server/',
    'toggle': 'http://localhost:5000/t.toggle/',
    'simulate': 'http://localhost:5000/t.simulate/',
}


def test_polling_endpoint(endpoint):
    task_id = endpoint.split('/')[-1]
    start_time = time()
    response = requests.get(endpoint)
    end_time = time()
    print(
        f'-------Requesting the Polling Endpoint took {end_time - start_time} seconds----\n')
    if response.json()['status_code'] == 400:
        try:
            assert response.status_code == 400
        except AssertionError:
            print('error testing status_code 400')
            print(
                f'Expected status code 400, recieved {response.status_code}')
            return response.json()

        try:
            assert response.status_code == response.json()['status_code']
        except AssertionError:
            print('error testing status_code 400')
            print(
                f'Expected paylod and response object to be the same\nPayload:{response.json()}\nResponse:{response.status_code}')
            return response.json()

    if response.json()['state'] == 'FAILURE':
        try:
            assert response.status_code == 500
        except AssertionError:
            print('error testing state FAILURE')
            print(
                f'Expected status code 500, recieved {response.status_code}')
            return response.json()

        try:
            assert response.status_code == response.json()['status_code']
        except AssertionError:
            print('error testing state FAILURE')
            print(
                f'Expected paylod and response object to be the same\nPayload:{response.json()}\nResponse:{response.status_code}')
            return response.json()

        try:
            assert response.json()['task_id'] == task_id
        except AssertionError:
            print('error testing state FAILURE')
            print(
                f'Expected task_id to be {task_id}, recieved {response.json()["task_id"]}')
            return response.json()

    if response.json()['state'] == 'PENDING':
        try:
            assert response.status_code == 200
        except AssertionError:
            print('error testing state PENDING')
            print(
                f'Expected status code 200, recieved {response.status_code}')
            return response.json()

        try:
            assert response.status_code == response.json()['status_code']
        except AssertionError:
            print('error testing state PENDING')
            print(
                f'Expected paylod and response object to be the same\nPayload:{response.json()}\nResponse:{response.status_code}')
            return response.json()

        try:
            assert response.json()['task_id'] == task_id
        except AssertionError:
            print('error testing state PENDING')
            print(
                f'Expected task_id to be {task_id}, recieved {response.json()["task_id"]}')
            return response.json()

    if response.json()['state'] == 'SUCCESS':
        try:
            assert response.status_code == 200
        except AssertionError:
            print('error testing state SUCCESS')
            print(
                f'Expected status code 200, recieved {response.status_code}')
            return response.json()

        try:
            assert response.status_code == response.json()['status_code']
        except AssertionError:
            print('error testing state SUCCESS')
            print(
                f'Expected paylod and response object to be the same\nPayload:{response.json()}\nResponse:{response.status_code}')

            return response.json()

        try:
            assert response.json()['task_id'] == task_id
        except AssertionError:
            print('error testing state SUCCESS')
            print(
                f'Expected task_id to be {task_id}, recieved {response.json()["task_id"]}')
            return response.json()

        try:
            assert response.json()['data'] is not None
        except AssertionError:
            print('error testing state SUCCESS')
            print(
                f'Expected result, recieved None\nResponse:{response.json()}')
            return response.json()
    return response.json()


def test_sanity_endpoint():
    try:
        start_time = time()
        response = requests.get(endpoint['sanity'])
        end_time = time()
        print(
            f'Requesting the Sanity Endpoint took {end_time - start_time} seconds')
        assert response.json()['data'] == "Hello, World!"
        assert response.status_code == 200
        assert response.status_code == response.json()['status_code']

    except AssertionError:
        print('Sanity endpoint failed')
        return (response.text)

    return (response.text)


def test_task_testing_endpoint():
    start_time = time()
    response = requests.get(endpoint['test_tasks'])
    end_time = time()
    print(
        f'Requesting the Test Tasks Endpoint took {end_time - start_time} seconds')
    try:
        assert response.status_code == 202
    except AssertionError:
        print(
            f'Recieved a bad response from the test_tasks endpoint\nStatus Code:{response.status_code}')
        return response.json()

    try:
        assert response.status_code == response.json()['status_code']
    except AssertionError:
        print(
            f'Expected paylod and response object to be the same\nPayload:{response.json()}\nResponse:{response.status_code}')
        return response.json()

    try:
        assert response.json()['task_id'] is not None
    except AssertionError:
        print(f'No task_id found in response\nResponse:{response.json()}')
        return response.json()

    try:
        assert response.json()['endpoint'] is not endpoint['poll']
    except AssertionError:
        print(f'No task id returned in response\nResponse:{response.json()}')
        return response.json()

    return response.json()['endpoint']


def test_sanity_and_polling():
    print(test_sanity_endpoint())
    endpoint = test_task_testing_endpoint()
    task_query = test_polling_endpoint(endpoint)
    while task_query['state'] != 'SUCCESS':
        sleep(8)
        task_query = test_polling_endpoint(endpoint)
        print(f"-------------\nRESPONSE:\n{task_query}\n-------------")
    if task_query['state'] == 'SUCCESS':
        print(
            f"-------------\nEXECUTION COMPLETE:\n{task_query}\n-------------")


def test_upload():
    from static import test_movies, test_servers
    media_tasks = []
    server_tasks = []
    for server in test_servers:
        response = requests.post(
            'http://localhost:5000/a.post-server/', json=server)
        server_tasks.append(response.json()['endpoint'])
    for movie in test_movies:
        response = requests.post(
            'http://localhost:5000/a.post-media/', json=movie)
        media_tasks.append(response.json()['endpoint'])
    return media_tasks, server_tasks


def test_upload_result(tasks):
    for task in tasks:
        task_query = test_polling_endpoint(task)
        while task_query['state'] != 'SUCCESS':
            task_query = test_polling_endpoint(task)
            print(f"-------------\nRESPONSE:\n{task_query}\n-------------")
        if task_query['state'] == 'SUCCESS':
            print(
                f"-------------\nEXECUTION COMPLETE:\n{task_query}\n-------------")
        return task_query


def test_upload_and_response():
    media_tasks, server_tasks = test_upload()
    media_dicts = []
    server_dicts = []
    for media_task in media_tasks:
        media_task_query = test_upload_result(media_task)
        media_dicts.append(media_task_query)
    for server_task in server_tasks:
        server_task_query = test_upload_result(server_task)
        server_dicts.append(server_task_query)
    for media_dict in media_dicts:
        assert media_dict['data']['server_list'] != []
    for server_dict in server_dicts:
        assert server_dict['data']['media_ids'] != []
    return media_dicts, server_dicts


def test_simulate_latency():
    start_time = time()
    response = requests.get(endpoint['simulate'])
    end_time = time()
    print(
        f'Requesting the Simulate Endpoint took {end_time - start_time} seconds')
    task_query = test_polling_endpoint(response.json()['endpoint'])
    while task_query['state'] != 'SUCCESS':
        task_query = test_polling_endpoint(response.json()['endpoint'])
        print(f"-------------\nRESPONSE:\n{task_query}\n-------------")
    if task_query['state'] == 'SUCCESS':
        print(
            f"-------------\nEXECUTION COMPLETE:\n{task_query}\n-------------")
    return task_query


def test_toggle_servers():
    start_time = time()
    response = requests.get(endpoint['toggle'])
    end_time = time()
    print(
        f'Requesting the Toggle Endpoint took {end_time - start_time} seconds')
    task_query = test_polling_endpoint(response.json()['endpoint'])
    while task_query['state'] != 'SUCCESS':
        task_query = test_polling_endpoint(response.json()['endpoint'])
        print(f"-------------\nRESPONSE:\n{task_query}\n-------------")
    if task_query['state'] == 'SUCCESS':
        print(
            f"-------------\nEXECUTION COMPLETE:\n{task_query}\n-------------")
    return task_query


def config_test_env():
    test_sanity_and_polling()
    test_upload_and_response()
    test_toggle_servers()
    test_simulate_latency()


if __name__ == '__main__':
    config_test_env()

    # threads = []

    # num_threads = 5

    # for _ in range(num_threads):
    #     thread = threading.Thread(target=test_upload_and_response)
    #     threads.append(thread)
    #     thread.start()

    # for thread in threads:
    #     thread.join()
