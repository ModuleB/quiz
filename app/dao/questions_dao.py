from flask_restx import abort

from app.dao.models import Question


class QuestionDAO:
    def __init__(self, session):
        self.session = session

    def safe_object(self, object):
        try:
            self.session.add(object)
            self.session.commit()
        except Exception:
            abort(500, "Ошибка базы данных")

    def safe_objects(self, objects):
        try:
            self.session.add_all(objects)
            self.session.commit()
        except Exception:
            abort(500, "Ошибка базы данных")

    def get_last(self):
        try:
            return self.session.query(Question).order_by(Question.id.desc()).first()
        except Exception:
            abort(500, "Ошибка базы данных")

    def is_exist(self, question):
        try:
            return self.session.query(Question).filter(Question.question == question).first()
        except Exception:
            abort(500, "Ошибка базы данных")

    def total_count(self):
        try:
            return self.session.query(Question).count()
        except Exception:
            abort(500, "Ошибка базы данных")
