import pytest
from main.dao.post_dao import PostsDAO

posts = PostsDAO()
post_keys = {
    "poster_name",
    "poster_avatar",
    "pic",
    "content",
    "views_count",
    "likes_count",
    "pk"
}


class TestPostDAO:
    def test_get_posts(self):
        assert isinstance(posts.get_posts(), list), "Не является списком"
        for post in posts.get_posts():
            assert post.keys() == post_keys, "Нет нужного ключа в одном из словарей"

    def test_get_posts_by_user(self):
        assert isinstance(posts.get_posts_by_user("leo"), list), "Не является списком"
        for post in posts.get_posts_by_user("leo"):
            assert post.keys() == post_keys, "Нет нужного ключа в одном из словарей"

    def test_get_search_for_posts(self):
        assert isinstance(posts.get_search_for_posts("в"), list), "Не является списком"
        for post in posts.get_search_for_posts("в"):
            assert post.keys() == post_keys, "Нет нужного ключа в одном из словарей"

    def test_get_post_pk(self):
        assert isinstance(posts.get_post_pk(1), dict), "Не является словарем"
        assert posts.get_post_pk(1).keys() == post_keys, "Нет нужного ключа в словаре"
