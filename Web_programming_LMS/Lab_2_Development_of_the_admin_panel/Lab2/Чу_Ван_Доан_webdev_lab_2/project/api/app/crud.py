from sqlalchemy.orm import Session
from sqlalchemy import or_
from . import models

def get_students(db: Session, skip: int, limit: int, filters: dict):
    query = db.query(models.Student)
    for field, value in filters.items():
        if value:
            query = query.filter(getattr(models.Student, field).ilike(f"%{value}%"))
    return query.offset(skip).limit(limit).all()
