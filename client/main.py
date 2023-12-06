import requests

PATHS = {
    "get_endpoint": "http://localhost:5000/c.get-media/",
    "get_all_media": "http://localhost:5000/c.get-list/",
}


def get_task_status(endpoint):
    response = requests.get(endpoint)  # Extract the "endpoint" key
    if response.json()["state"] == "SUCCESS":
        return response.json()
    elif response.json()["state"] == "FAILURE":
        return response.json()["traceback"]
    else:
        get_task_status(endpoint)


def get_media_endpoint(id):
    response = requests.get(PATHS["get_endpoint"], json={"id": 1})
    poll_endpoint = response.json()['endpoint']
    poll_reponse = get_task_status(poll_endpoint)
    return poll_reponse


def get_media_list():
    response = requests.get(PATHS["get_all_media"])
    poll_endpoint = response.json()['endpoint']  # Extract the "endpoint" key
    poll_reponse = get_task_status(poll_endpoint)
    return poll_reponse


def main():
    media_list = get_media_list()
    for media in media_list['data']:
        media_id = media["id"]
        endpoint = f"{PATHS['get_endpoint']}{int(media_id)}"
        media_endpoint = get_media_endpoint(endpoint)
        print('endpoint found')
        print({'endpoint': media_endpoint['data']['endpoint'],
              'latency': media_endpoint['data']['latency']})


if __name__ == "__main__":
    main()
