import requests
import json


def test_deployed_uniform():
    resp = requests.get("http://localhost:8000/uniform/10")

    assert resp.status_code == 200
    body = json.loads(resp.content)

    assert len(body['values']) == 10
