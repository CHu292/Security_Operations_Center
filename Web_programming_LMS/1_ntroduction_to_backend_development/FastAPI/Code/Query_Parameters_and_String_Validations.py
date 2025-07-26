from typing import Optional

from fastapi import FastAPI, Query

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(None, max_length=50)):
    results = {"items": [{"item_id": "Chu"}, {"item_id": "miran"}]}
    if q:
        results.update({"q": q})
    return results
