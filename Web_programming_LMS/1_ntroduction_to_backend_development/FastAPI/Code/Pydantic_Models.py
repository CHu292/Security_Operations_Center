from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel #import class BaseModel của thư viện pydantic

class Item(BaseModel): #Kế thừa từ class BaseModel và khai báo các biến
	name: str
	description: Optional[str] = None
	price: float
	tax: Optional[float] = None

app = FastAPI()

@app.post("/items/")
async def create_item(item: Item): #Khai báo dưới dạng parameter
	return item
