import json
from config import COMMENTS_DATA


class CommentsDAO:
    def __init__(self, path=COMMENTS_DATA):
        self.path = path

    def get_comments(self):
        with open(self.path, 'r', encoding="UTF-8") as file:
            all_comments = json.load(file)
            return all_comments

    def get_comments_id(self, post_id):
        all_comments = self.get_comments()
        comments_by_post_id = [c for c in all_comments if post_id == c["post_id"]]

        return comments_by_post_id

