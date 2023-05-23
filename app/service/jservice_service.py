from app.dao.jservice_dao import JserviceDAO


class JserviceService:
    def __init__(self, dao: JserviceDAO):
        self.dao = dao

    def get_questions(self, number):
        return self.dao.get_questions(number)
