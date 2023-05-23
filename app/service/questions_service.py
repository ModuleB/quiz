from app.dao.questions_dao import QuestionDAO


class QuestionService:
    def __init__(self, dao: QuestionDAO):
        self.dao = dao

    def safe_object(self, object):
        self.dao.safe_object(object)

    def get_last(self):
        return self.dao.get_last()



