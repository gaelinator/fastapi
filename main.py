from fastapi import FastAPI
from typing import Union

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id*2, "q": q}

@app.get("/users/{user_id}")
def get_user(user_id: str):
    return {"user_id": user_id}