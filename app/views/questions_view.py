from flask import request, jsonify
from flask_restx import Namespace, Resource, abort

from app.container import question_service, jservice_service

questions_ns = Namespace('/questions')


@questions_ns.route("/")
class QuestionsView(Resource):
    def post(self):
        # Получаем данные запроса
        data = request.json
        questions_num = data.get("questions_num")


        # Получаем из базы последний сохраненный вопрос
        last_question = question_service.get_last()



        # Проверяем, задано ли поле 'questions_num'
        if not questions_num:
            abort(400, "В запросе отсутствует обязательный параметр 'questions_num' или его значение не задано")

        # Проверяем есть ли число в запросе
        try:
            questions_num = int(questions_num)
        except:
            abort(400, "Параметр 'questions_num' должен быть числом")

        # Проверяем, что 'questions_num' больше 0 и меньше или равно 500
        if not 0 < questions_num <= 500:
            abort(400, "Параметр 'questions_num' выходит за пределы допустимых значений (от 1 до 500)")

        #  Заполняем список вопросами, для сохранения в базе.
        #  Количество вопросов равно 'questions_num'
        questions_to_safe = []
        questions_to_safe_num = 0

        while questions_to_safe_num < questions_num:

            # Проверка, чтобы в первую итерацию цикла не выводить надпись '0'
            if questions_to_safe_num != 0:
                print(f"Сохранено вопросов {questions_to_safe_num}")

            # Загружаем вопросы с сервера
            questions = jservice_service.get_questions()


            # Заполняем список вопросов
            for question in questions:

                # Если в списке достаточно вопросов, выходим
                if questions_to_safe_num == questions_num:
                    break

                # Добавляем вопрос в список, если его не существует
                if question_service.is_exist(question) is not True:
                    questions_to_safe.append(question)
                    questions_to_safe_num = len(questions_to_safe)

        # Сохраняем вопросы в базе данных
        question_service.safe_questions(questions_to_safe)

        print(f"Сохранено вопросов: {questions_to_safe_num}")
        print(f"Всего вопросов в базе: {question_service.total_count()}")


        # Формируем ответ, если последний вопрос найден
        if last_question:
            response = jsonify({"previous_question": last_question.question})
        else:
            response = jsonify()

        # Возвращаем 'last_question'
        return response
