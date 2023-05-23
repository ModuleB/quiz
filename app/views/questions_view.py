from flask import request, jsonify
from flask_restx import Namespace, Resource

from app.container import question_service, jservice_service
from app.dao.models import Question

questions_ns = Namespace('/questions')


@questions_ns.route("/")
class QuestionsView(Resource):
    def post(self):
        # Получаем данные запроса
        data = request.json
        # Получаем из базы последний сохраненный вопрос
        last_question = question_service.get_last()
        try:
            # Проверяем есть ли число в запросе
            questions_num = int(data.get("questions_num"))
        except:
            response = jsonify()
            response.status_code = 400
            return response
        else:
            """1. Получаем в два раза больше вопросов от сервера jservice, чем требовалось, для того,
            чтобы не запрашивать еще раз, если вопрос уже существует в базе.
            2. Сохраняем по одному вопросу в базу.
            Если ошибка (в поле question должно быть уникальное значение), то итерируемся дальше по вопросам
            Если и их не хватит, то запрашиваем сервер jservice еще раз"""

            questions_saved = 0
            while questions_saved < questions_num:
                questions = jservice_service.get_questions(questions_num * 2)
                for question in questions:
                    if questions_saved == questions_num:
                        break
                    obj = Question(
                        question=question["question"],
                        right_answer=question["answer"],
                        question_id=question["id"],
                        created_at=question["created_at"]
                    )
                    try:
                        question_service.safe_object(obj)
                        questions_saved += 1
                    except:
                        continue

            if last_question:
                response = jsonify({"previous_question": last_question.question})
            else:
                response = jsonify()
                response.status_code = 404
            return response
