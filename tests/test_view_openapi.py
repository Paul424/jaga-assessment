import yaml


def test_openapi_get(client):
    response = client.get("/openapi.yaml")
    assert response.status_code == 200
    assert response.mimetype == "application/x-yaml"
    document = yaml.safe_load(response.data.decode("utf-8"))
    assert "/tasks/" in document["paths"]
