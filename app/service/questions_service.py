from app.dao.models import Question
from app.dao.questions_dao import QuestionDAO


class QuestionService:
    def __init__(self, dao: QuestionDAO):
        self.dao = dao

    def safe_question(self, question):
        self.dao.safe_object(self._create_obj(question))

    def safe_questions(self, questions):
        objects = []
        for question in questions:
            objects.append(self._create_obj(question))
        self.dao.safe_objects(objects)

    def is_exist(self, question):
        if self.dao.is_exist(question["question"]):
            return True

    def get_last(self):
        return self.dao.get_last()

    def total_count(self):
        return self.dao.total_count()

    def _create_obj(self, question):
        return Question(
            question=question["question"],
            right_answer=question["answer"],
            question_id=question["id"],
            created_at=question["created_at"]
        )

