from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Request schema
class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

# Basic GET endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to My API!"}

# POST endpoint
@app.post("/items/")
def create_item(item: Item):
    return {"item": item}

# Run server: uvicorn main:app --reload
