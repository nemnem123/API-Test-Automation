import requests

BASE_URL = "https://i4gwcc0h4h.execute-api.ap-southeast-2.amazonaws.com/dev"


def clean_db():
    
    requests.delete(f"{BASE_URL}/echo")


def test_get_hello():
    r = requests.get(f"{BASE_URL}/hello")
    assert r.status_code == 200



def test_post_echo():
    
    clean_db()

    payload = {
        "name": "ngungu",
        "role": "student"
    }

    r = requests.post(f"{BASE_URL}/echo", json=payload)
    assert r.status_code == 201


def test_get_echo_after_post():
    
    clean_db()

    payload = {
        "name": "ngungu",
        "role": "student"
    }

    # POST trước
    r = requests.post(f"{BASE_URL}/echo", json=payload)
    assert r.status_code == 201

    # GET sau
    r = requests.get(f"{BASE_URL}/echo")
    assert r.status_code == 200

    data = r.json()
    assert isinstance(data, list)
    assert len(data) >= 1


def test_delete_echo():
    

    # 1. Chuẩn bị dữ liệu (POST)
    payload = {
        "name": "ngungu",
        "role": "student"
    }

    r = requests.post(f"{BASE_URL}/echo", json=payload)
    assert r.status_code == 201

    # 2. Thực hiện DELETE
    r = requests.delete(f"{BASE_URL}/echo")

    # 3. DELETE thành công: REST cho phép 200 hoặc 204
    assert r.status_code in (200, 204)
def test_invalid_input_type():
    

    payload = {
        "name": 123,          # sai kiểu
        "role": "student"
    }

    r = requests.post(f"{BASE_URL}/echo", json=payload)

    # Kỳ vọng API từ chối dữ liệu sai
    assert r.status_code == 400
