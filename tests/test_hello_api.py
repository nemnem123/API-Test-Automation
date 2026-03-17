import requests

BASE_URL = "https://i4gwcc0h4h.execute-api.ap-southeast-2.amazonaws.com/dev"


def test_get_hello():

    r = requests.get(f"{BASE_URL}/hello")
    print(f"Status: {r.status_code}, Body: {r.text}")

    assert r.status_code == 200


def test_post_echo():

    payload = {
        "name": "ngungu",
        "role": "student"
    }

    r = requests.post(f"{BASE_URL}/echo", json=payload)

    assert r.status_code == 201


def test_get_echo_after_post():

    payload = {
        "name": "ngungu",
        "role": "student"
    }

    requests.post(f"{BASE_URL}/echo", json=payload)

    r = requests.get(f"{BASE_URL}/echo")

    assert r.status_code == 200


def test_delete_echo():

    payload = {
        "name": "ngungu",
        "role": "student"
    }

    requests.post(f"{BASE_URL}/echo", json=payload)

    r = requests.delete(f"{BASE_URL}/echo")

    assert r.status_code == 200


def test_invalid_input_type():

    payload = {
        "name": 123,
        "role": "student"
    }

    r = requests.post(f"{BASE_URL}/echo", json=payload)

    assert r.status_code == 201