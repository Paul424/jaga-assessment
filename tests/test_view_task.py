# list
def test_tasks_get_empty(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_tasks_get_3_items(client):
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 3


# create

# update

# delete
