from app.dao.models import Question


class QuestionDAO:
    def __init__(self, session):
        self.session = session

    def safe_object(self, object):
        self.session.add(object)
        self.session.commit()

    def get_last(self):
        return self.session.query(Question).order_by(Question.id.desc()).first()


