# tests/test_users.py

import pytest
from utils.payloads import PayloadBuilder
from assertpy import assert_that

@pytest.mark.sanity
def test_get_users(user_api):
    res = user_api.get_users()
    assert res.status_code == 200
    assert_that(res.status_code).is_equal_to(200, msg="Status code mismatch")
    assert len(res.json()) > 5

@pytest.mark.positive
def test_get_user_by_name(user_api):
    res = user_api.get_user_by_name("Sherry Auer")
    assert res.status_code == 200
    assert res.json()[0]["id"] == "6"

@pytest.mark.negative
@pytest.mark.parametrize("user_id, expected_status", [(1, 200), (9999, 404)])
def test_get_user_by_id(user_api, user_id, expected_status):
    res = user_api.get_user(user_id)
    assert res.status_code == expected_status

@pytest.mark.positive
def test_create_user(user_api):
    payload = (
        PayloadBuilder()
        .add("name", "New Test User")
        .add("createdAt", "2025-08-03T00:00:00.000Z")
        .build()
    )
    res = user_api.create_user(payload)
    assert res.status_code == 201
    assert res.json()["name"] == "New Test User"

    res_get = user_api.get_user_by_name("New Test User")
    assert res_get.status_code == 200
    assert any(user["name"] == "New Test User" for user in res_get.json())

@pytest.mark.positive
def test_delete_user(user_api):
    res =user_api.delete_user("9")
    assert res.status_code == 200
    res_get = user_api.get_user_by_name("9")
    assert res_get.status_code == 404
