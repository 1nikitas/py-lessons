from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, Numeric
from database import Base

class Answer(Base):
    __tablename__ = 'user_answers'

    answer_id = Column(Integer, primary_key=True)
    answer = Column(String)
    user_id = Column(Integer)
    alternatives_id = Column(Integer)

class Question(Base):
    __tablename__ = 'user_questions'

    question_id = Column(Integer, primary_key=True)
    question = Column(String)
    user_id = Column(Integer)

class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    mail = Column(String)
    phone = Column(String)

