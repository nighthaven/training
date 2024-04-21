from typing import Union
from fastapi import FastAPI
from src.route.characters_route import path as characters_path
from src.Models import engine, characters_models


app = FastAPI()

app.include_router(characters_path)

#characters_models.Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}