import requests


def create_obj():
    payload = {
        "name": "XIaomi band Mi-5",
        "data": {
            "year": 2021,
            "price": 30.11,
            "CPU model": "CPU",
            "Hard disk size": "512 MB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    return response['id']


def test_create_object():
    payload = {
        "name": "XIaomi band Mi-5",
        "data": {
            "year": 2021,
            "price": 30.11,
            "CPU model": "CPU",
            "Hard disk size": "512 MB"
        }
    }
    response = requests.post('https://api.restful-api.dev/objects', json=payload).json()
    assert response['name'] == payload['name']
    print(response)


def test_get_object():
    obj_id = create_obj()
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}').json()
    assert response['id'] == obj_id


def test_update_object():
    obj_id = create_obj()
    payload = {
            "name": "Samsung",
            "data": {
                "year": 2023,
                "price": 310.11,
                "CPU model": "CPU",
                "Hard disk size": "512 MB"
            }
        }
    response = requests.put(
        f'https://api.restful-api.dev/objects/{obj_id}',
        json=payload
    ).json()
    print(response)
    assert response['name'] == payload['name']


def test_delete_object():
    obj_id = create_obj()
    response = requests.delete(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 200
    response = requests.get(f'https://api.restful-api.dev/objects/{obj_id}')
    assert response.status_code == 404
    print(response)
