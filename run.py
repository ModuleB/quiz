from flask import Flask
from flask_restx import Api
from waitress import serve

from app.config import config
from app.views.questions_view import questions_ns


if __name__ == "__main__":

    app = Flask("app")

    # Загрузка конфигурации
    app.config.from_object(config)
    app.app_context().push()

    # Регистрация restx
    api = Api(app)
    # Регистрация неймспейсов
    api.add_namespace(questions_ns)

    # Запуск
    if app.config.get("FLASK_ENV") == "production":
        serve(app, host="0.0.0.0", port=80)
    else:
        app.run(host="0.0.0.0", port=80)
