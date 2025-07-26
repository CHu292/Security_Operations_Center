from pydantic import BaseModel

class StudentBase(BaseModel):
    Фамилия: str
    Имя: str
    Отчество: str
    Курс: str
    Группа: str
    Факультет: str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
