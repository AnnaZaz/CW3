from os import path

parent_dir = path.dirname(path.abspath(__file__))
POSTS_DATA = path.join(parent_dir, 'data', 'data.json')  # путь к данным постов
COMMENTS_DATA = path.join(parent_dir, 'data', 'comments.json')  # путь к данным комментариев
BOOKMARKS_DATA = path.join(parent_dir, 'data', 'bookmarks.json')  # путь к данным закладок
LOG_PATH = path.join(parent_dir, 'logs', 'api.log')  # путь к данным логов

