from flask_restx import abort

from app.dao.jservice_dao import JserviceDAO


class JserviceService:
    def __init__(self, dao: JserviceDAO):
        self.dao = dao

    def get_questions(self):

        data = self.dao.get_questions()

        # Проверяем наличие нужных нам ключей
        if not data:
            abort(500, "Ошибка при обращении к внешнему ресурсу")

        keys = set(data[0].keys())
        needed_keys = set(("id", "question", "answer", "created_at"))

        if not needed_keys.issubset(keys):
            abort(500, "Нет нужных ключей в ответе сервера jservice")

        return data

