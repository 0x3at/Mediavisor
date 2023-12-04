import requests


def test_isAlive_endpoint():
    try:
        response = requests.get("http://127.0.0.1:5000/isAlive/ping")
        assert response.status_code == 200
        print(response.json()["message"])
    except Exception:
        print(f"Bad status code : {response.status_code}")
        raise AssertionError


if __name__ == "__main__":
    print('Testing "isAlive/ping" endpoint...')
    test_isAlive_endpoint()
