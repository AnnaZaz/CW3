from flask import Blueprint, render_template, request, abort
from main.dao.post_dao import PostsDAO
from main.dao.comments_dao import CommentsDAO

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    posts = PostsDAO().get_posts()
    return render_template("index.html", posts=posts)


@main_blueprint.route("/post/<int:post_id>/")
def page_post(post_id):
    post = PostsDAO().get_post_pk(post_id)
    if post is None:
        return abort(404)
    comments = CommentsDAO().get_comments_id(post_id)
    return render_template("post.html", post=post, comments=comments)


@main_blueprint.route("/search/", methods=["GET"])
def search_page():
    posts = ""
    if request.values.get("s"):
        query = request.values.get("s")
        posts = PostsDAO().get_search_for_posts(query)
    return render_template("search.html", posts=posts)


@main_blueprint.route("/user/<name>/")
def user_page(name):
    posts = PostsDAO().get_posts_by_user(name)
    return render_template("user-feed.html", posts=posts)

