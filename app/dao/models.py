from sqlalchemy import String, Integer, TIMESTAMP, Column
from app.database import db, engine, db_session


class Question(db):
    __tablename__ = 'quiz'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    question_id = Column(String, nullable=False, unique=True)
    question = Column(String, nullable=False, unique=True)
    right_answer = Column(String, nullable=False)
    created_at = Column(TIMESTAMP, nullable=False)

    def __repr__(self):
        return f'{self.question_id}\n{self.question}\n{self.created_at}'

# db.metadata.drop_all(engine)
db.metadata.create_all(engine)
db_session.commit()
