import pytest
from run import app

dct_keys = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk"
}


def test_all_json_posts():
    response = app.test_client().get("/api/posts/")
    assert isinstance(response.json, list), "Не является списком"
    for dct in response.json:
        assert dct.keys() == dct_keys, "В одном из словарей не хватает ключей"


def test_json_post():
    response = app.test_client().get("/api/posts/1/")
    assert isinstance(response.json, dict), "Не является словарем"
    assert response.json.keys() == dct_keys, "Не хватает ключей"
