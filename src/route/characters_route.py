from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.repository import characters_repository
from src.serializer.characters import CharactersSerializer
from src.Models import get_db

path = APIRouter()

@path.get("/heroes")
def get_characters(db: Session = Depends(get_db)):
    characters = characters_repository.get_characters(db)
    return [CharactersSerializer(character) for character in characters]