import requests
from flask_restx import abort


class JserviceDAO():
    def get_questions(self):

        # Получаем вопросы от сервера
        try:
            response = requests.get(f"http://jservice.io/api/random?count=100")
            print("Запрос сервера")
            return response.json()
        except Exception:
            abort(500, "Ошибка при обращении к внешнему ресурсу")


