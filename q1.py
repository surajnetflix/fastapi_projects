from fastapi import FastAPI

app = FastAPI()

# Q1. A user calls GET /users/me and gets a 422 error. Fix it without changing the paths.
'''
404 Not Found: The server cannot find the requested URL or resource identifier.
422 Unprocessable Content: The request is well-formed (valid syntax), but the content contains logical errors.

Resolution: Write get_me method before get_user

'''

@app.get("/users/me")
async def get_me():
    return {"user": "me"}


@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}

# @app.get("/users/me")
# async def get_me():
#     return {"user": "me"}
