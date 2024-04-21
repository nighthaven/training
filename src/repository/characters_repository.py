from sqlalchemy.orm import Session
from fastapi import Depends
from src.Models import get_db, characters_models



def get_characters(db: Session = Depends(get_db)):
    return db.query(characters_models.Characters).all()