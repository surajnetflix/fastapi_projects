# Q2. GET /items/5 returns {"id": "5"} (a string). It should return {"id": 5}, and /items/x should
# return 422. Fix it.


'''
Resolution: Added 'int' for function parameter
'''
from fastapi import FastAPI

app = FastAPI()

# @app.get("/items/{item_id}")
# async def get_item(item_id):
#     return {"id": item_id}

@app.get("/items/{item_id}")
async def get_item(item_id: int):
    return {"id": item_id}
