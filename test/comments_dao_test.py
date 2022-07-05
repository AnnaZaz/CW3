import pytest
from main.dao.comments_dao import CommentsDAO

comments = CommentsDAO()
comment_keys = {
    "post_id",
    "commenter_name",
    "comment",
    "pk",
}


class TestCommentsDAO:
    def test_get_comments(self):
        assert isinstance(comments.get_comments(), list), "Не является списком"
        for comment in comments.get_comments():
            assert comment.keys() == comment_keys, "Нет нужного ключа в одном из словарей"

    def test_get_comments_id(self):
        assert isinstance(comments.get_comments_id(1), list), "Не является списком"
        for comment in comments.get_comments_id(1):
            assert comment.keys() == comment_keys, "Нет нужного ключа в одном из словарей"
