import json
from config import POSTS_DATA


class PostsDAO:
    def __init__(self, path=POSTS_DATA):
        self.path = path

    def get_posts(self):
        with open(self.path, 'r', encoding="UTF-8") as file:
            posts = json.load(file)
            return posts

    def get_posts_by_user(self, name):
        all_posts = self.get_posts()
        for post in all_posts:
            if post["poster_name"].lower().strip() == name.lower().strip():
                break
        else:
            raise ValueError("Такого пользователя нет")

        posts_by_user = []
        for post in all_posts:
            if post["poster_name"].lower().strip() == name.lower().strip():
                posts_by_user.append(post)

        return posts_by_user

    def get_search_for_posts(self, query):
        all_posts = self.get_posts()
        search_posts = []
        for post in all_posts:
            if query.lower().strip() in post["content"]:
                search_posts.append(post)

        return search_posts

    def get_post_pk(self, pk):
        all_posts = self.get_posts()
        for post in all_posts:
            if post["pk"] == pk:
                return post



