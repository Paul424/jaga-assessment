import pytest

# list


@pytest.mark.parametrize(
    "method_name",
    [
        # pytest.param("get", id="GET"),
        # pytest.param("head", id="HEAD"),
        # pytest.param("post", id="POST"),
        pytest.param("put", id="PUT"),
        pytest.param("delete", id="DELETE"),
        # pytest.param("options", id="OPTIONS"),
        pytest.param("trace", id="TRACE"),
        pytest.param("patch", id="PATCH"),
    ],
)
def test_tasks_get_not_allowed(client, no_oauth, method_name):
    response = getattr(client, method_name)("/tasks/")
    assert response.status_code == 405  # METHOD NOT ALLOWED


def test_tasks_head(client, no_oauth):
    response = client.head("/tasks/")
    assert response.status_code == 200


def test_tasks_options(client, no_oauth):
    response = client.options("/tasks/")
    assert response.status_code == 200
    assert response.allow.as_set() == set(["post", "get", "head", "options"])


def test_tasks_get_empty(client, no_oauth):
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 0


def test_tasks_get_2_items(client, no_oauth, task_factory):
    task1 = task_factory(username="Fred Flintstone", email="fred.flintstone@gmail.com")
    task2 = task_factory(
        username="Wilma Flintstone", email="wilma.flintstone@gmail.com"
    )
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) == 2


@pytest.mark.parametrize(
    "page, per_page, expected",
    [
        (1, None, ["fred", "wilma", "barney", "betty", "bammbamm"]),
        (None, 5, ["fred", "wilma", "barney", "betty", "bammbamm"]),
        (1, 5, ["fred", "wilma", "barney", "betty", "bammbamm"]),
        (2, 5, []),
        (1, 3, ["fred", "wilma", "barney"]),
        (2, 3, ["betty", "bammbamm"]),
        (3, 3, []),
        (1, 25, ["fred", "wilma", "barney", "betty", "bammbamm"]),
    ],
)
def test_tasks_get_paginate(client, no_oauth, task_factory, page, per_page, expected):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    task2 = task_factory(username="wilma", email="wilma.flintstone@gmail.com")
    task3 = task_factory(username="barney", email="barney.rubble@gmail.com")
    task4 = task_factory(username="betty", email="betty.rubble@gmail.com")
    task5 = task_factory(username="bammbamm", email="bamm.bamm.rubble@gmail.com")
    query_params = []
    if page is not None:
        query_params.append(f"page={page}")
    if per_page is not None:
        query_params.append(f"per_page={per_page}")
    uri = f"/tasks/?{'&'.join(query_params)}"
    response = client.get(uri)
    assert response.status_code == 200
    data = response.get_json()
    assert [x["username"] for x in data] == expected


@pytest.mark.parametrize(
    "order_by, op, expected",
    [
        ("id", None, ["fred", "wilma", "barney", "betty", "bammbamm"]),
        ("id", "asc", ["fred", "wilma", "barney", "betty", "bammbamm"]),
        ("id", "desc", ["bammbamm", "betty", "barney", "wilma", "fred"]),
        ("username", "asc", ["bammbamm", "barney", "betty", "fred", "wilma"]),
        ("username", "desc", ["wilma", "fred", "betty", "barney", "bammbamm"]),
        ("email", "asc", ["bammbamm", "barney", "betty", "fred", "wilma"]),
        ("email", "desc", ["wilma", "fred", "betty", "barney", "bammbamm"]),
    ],
)
def test_tasks_get_order_by(client, no_oauth, task_factory, order_by, op, expected):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    task2 = task_factory(username="wilma", email="wilma.flintstone@gmail.com")
    task3 = task_factory(username="barney", email="barney.rubble@gmail.com")
    task4 = task_factory(username="betty", email="betty.rubble@gmail.com")
    task5 = task_factory(username="bammbamm", email="bamm.bamm.rubble@gmail.com")
    query_params = []
    if order_by is not None:
        query_params.append(f"order_by={order_by}")
    if op is not None:
        query_params.append(f"op={op}")
    response = client.get(f"/tasks/?{'&'.join(query_params)}")
    assert response.status_code == 200
    data = response.get_json()
    assert [x["username"] for x in data] == expected


# create


def test_tasks_create_no_data(client, no_oauth):
    response = client.post("/tasks/", json={})
    assert response.status_code == 422  # UNPROCESSABLE_CONTENT


def test_tasks_create_incomplete_data(client, no_oauth):
    response = client.post(
        "/tasks/",
        json={
            "username": "wilma",
        },
    )
    assert response.status_code == 422  # UNPROCESSABLE_CONTENT


def test_tasks_create_wrong_field(client, no_oauth):
    response = client.post(
        "/tasks/",
        json={
            "user": "wilma",
        },
    )
    assert response.status_code == 422  # UNPROCESSABLE_CONTENT


def test_tasks_create_validation_error_email(client, no_oauth):
    response = client.post(
        "/tasks/",
        json={
            "username": "wilma",
            "email": "not-an-email",
        },
    )
    assert response.status_code == 422  # UNPROCESSABLE_CONTENT


def test_tasks_create_ok(client, no_oauth):
    response = client.post(
        "/tasks/",
        json={
            "username": "wilma",
            "email": "wilma.flintstone@gmail.com",
        },
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["email"] == "wilma.flintstone@gmail.com"


# detail


@pytest.mark.parametrize(
    "method_name",
    [
        # pytest.param("get", id="GET"),
        # pytest.param("head", id="HEAD"),
        pytest.param("post", id="POST"),
        # pytest.param("put", id="PUT"),
        # pytest.param("delete", id="DELETE"),
        # pytest.param("options", id="OPTIONS"),
        pytest.param("trace", id="TRACE"),
        pytest.param("patch", id="PATCH"),
    ],
)
def test_tasks_create_not_allowed(client, no_oauth, task_factory, method_name):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = getattr(client, method_name)(
        f"/tasks/{task1.id}", json={"username": task1.username, "email": task1.email}
    )
    assert response.status_code == 405  # METHOD NOT ALLOWED


def test_tasks_head(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.head(f"/tasks/{task1.id}")
    assert response.status_code == 200


def test_tasks_options(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.options(f"/tasks/{task1.id}")
    assert response.status_code == 200
    assert response.allow.as_set() == set(["get", "delete", "put", "head", "options"])


# update


def test_tasks_update_item_not_found(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.put(
        f"/tasks/{task1.id + 1}",
        json={"username": task1.username, "email": task1.email},
    )
    assert response.status_code == 404


def test_tasks_update_same(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.put(
        f"/tasks/{task1.id}", json={"username": task1.username, "email": task1.email}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["username"] == task1.username
    assert data["email"] == task1.email


def test_tasks_update_changes(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.put(
        f"/tasks/{task1.id}",
        json={"username": "barney", "email": "barney.rubble@gmail.com"},
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["username"] == "barney"
    assert data["email"] == "barney.rubble@gmail.com"


# delete


def test_tasks_delete_item_not_found(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.delete(
        f"/tasks/{task1.id + 1}",
        json={"username": task1.username, "email": task1.email},
    )
    assert response.status_code == 404


def test_tasks_delete_item(client, no_oauth, task_factory):
    task1 = task_factory(username="fred", email="fred.flintstone@gmail.com")
    response = client.delete(
        f"/tasks/{task1.id}", json={"username": task1.username, "email": task1.email}
    )
    assert response.status_code == 204
