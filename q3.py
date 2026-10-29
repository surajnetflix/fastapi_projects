# Q3. This code crashes on startup with a SyntaxError. Fix it (keep token required and skip optional).

from fastapi import FastAPI
app = FastAPI()

'''
skip is a parameter with fallback value, such parameters should be at the end of the function params.
'''

# @app.get("/feed")
# async def feed(skip: int = 0, token: str):
#     return {"skip": skip, "token": token}

@app.get("/feed")
async def feed(token: str, skip: int = 0):
    return {"skip": skip, "token": token}
