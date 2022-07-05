from flask import Blueprint

blueprint_error = Blueprint("blueprint_error", __name__, template_folder="templates")


@blueprint_error.app_errorhandler(ValueError)
def page_value_error(e):
    return "Страница не найдена"

@blueprint_error.app_errorhandler(404)
def page_value_error(e):
    return "Страница не найдена"

@blueprint_error.app_errorhandler(500)
def page_value_error(e):
    return "Ошибка сервера"