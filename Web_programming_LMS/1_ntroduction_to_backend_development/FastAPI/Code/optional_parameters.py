from fastapi import FastAPI
from typing import Optional

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    '''
    param item_id: format string
    param q: format string, default value: None, Optional: help you find error that happen
    '''
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
