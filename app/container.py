from app.dao.jservice_dao import JserviceDAO
from app.dao.questions_dao import QuestionDAO
from app.database import db_session
from app.service.jservice_service import JserviceService
from app.service.questions_service import QuestionService

question_dao = QuestionDAO(db_session)
question_service = QuestionService(question_dao)
jservice_dao = JserviceDAO()
jservice_service = JserviceService(jservice_dao)
