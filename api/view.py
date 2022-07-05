import logging
from flask import Blueprint, jsonify
from main.dao.post_dao import PostsDAO
from config import LOG_PATH

api_blueprint = Blueprint("api_blueprint", __name__, template_folder="templates")

api_log = logging.getLogger("api_log")
api_log.setLevel(logging.INFO)
file_handler_api_log = logging.FileHandler(LOG_PATH, encoding="UTF-8")
api_log.addHandler(file_handler_api_log)

format_api_log = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
file_handler_api_log.setFormatter(format_api_log)


@api_blueprint.route("/posts/")
def all_json_posts():
    api_log.info("Запрос /api/posts/")
    posts = PostsDAO().get_posts()
    return jsonify(posts)


@api_blueprint.route("/posts/<int:post_id>/")
def json_post(post_id):
    api_log.info(f"Запрос /api/posts/{post_id}/")
    post = PostsDAO().get_post_pk(post_id)
    return jsonify(post)
