import pytest


def test_tasks_auth_get(client):
    response = client.get("/tasks/")
    assert response.status_code == 401

def test_tasks_auth_create(client):
    response = client.post("/tasks/", json={})
    assert response.status_code == 401

def test_tasks_auth_get(client):
    response = client.get(f"/tasks/1")
    assert response.status_code == 401

def test_tasks_auth_update(client):
    response = client.put(
        f"/tasks/1",
        json={"username": "dummy", "email": "dummy"},
    )
    assert response.status_code == 401

def test_tasks_auth_delete(client):
    response = client.delete(
        f"/tasks/1",
        json={"username": "dummy", "email": "dummy"},
    )
    assert response.status_code == 401
