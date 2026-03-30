from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: str | None = None

items = [
    {"id": 1, "name": "Sample Item", "description": "This is a sample item."}
]

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment."}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item.dict())
    return item

# Run the app with: uvicorn starter-code:app --reload
# Example requests:
# GET http://127.0.0.1:8000/
# GET http://127.0.0.1:8000/items
# POST http://127.0.0.1:8000/items with JSON body
