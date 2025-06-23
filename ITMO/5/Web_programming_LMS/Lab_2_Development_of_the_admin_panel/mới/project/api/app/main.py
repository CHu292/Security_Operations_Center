from fastapi import FastAPI, Depends, Query
from sqlalchemy.orm import Session
from . import models, schemas, crud
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/students/", response_model=list[schemas.Student])
def read_students(
    skip: int = 0,
    limit: int = 10,
    Фамилия: str = Query(None),
    Имя: str = Query(None),
    Отчество: str = Query(None),
    Курс: str = Query(None),
    Группа: str = Query(None),
    Факультет: str = Query(None),
    db: Session = Depends(get_db),
):
    filters = {
        "Фамилия": Фамилия,
        "Имя": Имя,
        "Отчество": Отчество,
        "Курс": Курс,
        "Группа": Группа,
        "Факультет": Факультет,
    }
    return crud.get_students(db, skip=skip, limit=limit, filters=filters)
