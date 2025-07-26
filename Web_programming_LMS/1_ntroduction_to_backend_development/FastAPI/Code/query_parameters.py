from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Ch"}, {"item_name": "Mi"}, {"item_name": "ran"}] # pair format: key-value

@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
	return fake_items_db[skip: skip+limit] # trả về dữ liệu từ skip đến skip  + limit

