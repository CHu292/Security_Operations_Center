from fastapi import FastAPI
app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, short: bool = False): # param short với định dạng boolean có giá trị mặc  định là Fase
	item = {"item_id": item_id}
	if not short:
		item.update(
			{"description": "This is an amazing item that has a long description"}
		)
	return item
