import requests

# Для запуска тестов необходимо:
# 1. Получить API token в. Yougile
# 2. Вставить его в переменную token ниже

base_url = "https://yougile.com"
token = "PASTE_TOKEN_HERE_PLS"


# создание проекта с авторизацией
def test_create_project_positive():
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "title": "Autotest_project"
    }

    response = requests.post(
        f"{base_url}/api-v2/projects",
        json=body,
        headers=headers
    )

    assert response.status_code == 201

    data = response.json()
    assert "id" in data
    assert data["id"] is not None


# создание проекта без авторизации
def test_create_project_negative():

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "title": "Negative_test_project"
    }

    response = requests.post(
        f"{base_url}/api-v2/projects",
        json=body,
        headers=headers
    )

    assert response.status_code == 401


# изменение проекта
def headers_with_token():
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


def create_project(title):
    body = {"title": title}
    return requests.post(
        f"{base_url}/api-v2/projects",
        json=body, headers=headers_with_token(),
        )


def update_project(project_id, new_title, headers):
    body = {"title": new_title}
    return requests.put(
        f"{base_url}/api-v2/projects/{project_id}",
        json=body, headers=headers,
    )


def test_update_project_positive():
    create_resp = create_project("Autotest_for_update")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    update_resp = update_project(
        project_id, "Autotest_UPDATED", headers_with_token(),
    )
    assert update_resp.status_code == 200

    data = update_resp.json()
    assert data["id"] == project_id


# изменение проекта без токена
def test_update_project_negative_no_auth():
    create_resp = create_project("Autotest_for_update_no_auth")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]

    no_auth_headers = {"Content-Type": "application/json"}
    update_resp = update_project(project_id, "NOT_UPDATE", no_auth_headers)

    assert update_resp.status_code == 401


# получение по ID
def get_project(project_id, headers):
    return requests.get(
        f"{base_url}/api-v2/projects/{project_id}",
        headers=headers,
    )


def test_get_project_positive():
    # создаём проект
    create_resp = create_project("Autotest_for_get")
    assert create_resp.status_code == 201
    project_id = create_resp.json()["id"]
    assert project_id is not None

    # получаем по id
    get_resp = get_project(project_id, headers_with_token())
    assert get_resp.status_code == 200

    data = get_resp.json()
    assert data["id"] == project_id


# получение по несуществующему ID
def test_get_project_negative_not_found():
    fake_id = "00000000-0000-0000-0000-000000000000"

    get_resp = get_project(fake_id, headers_with_token())
    assert get_resp.status_code == 404
