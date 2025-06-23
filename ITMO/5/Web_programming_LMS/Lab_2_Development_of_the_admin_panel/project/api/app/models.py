from sqlalchemy import Column, Integer, String
from .database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    Фамилия = Column(String, index=True)
    Имя = Column(String, index=True)
    Отчество = Column(String, index=True)
    Курс = Column(String, index=True)
    Группа = Column(String, index=True)
    Факультет = Column(String, index=True)
