import requests
import json


def test_uniform():
    resp = requests.get("http://localhost:8000/uniform/")

    assert resp.status_code == 200
    body = json.loads(resp.content)

    assert body['value']


def test_normal():
    resp = requests.get("http://localhost:8000/normal/")

    assert resp.status_code == 200
    body = json.loads(resp.content)

    assert body['value']


def test_exponential():
    resp = requests.get("http://localhost:8000/exponential/")

    assert resp.status_code == 200
    body = json.loads(resp.content)

    assert body['value']
