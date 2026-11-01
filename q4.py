# Q4. Write the status code and JSON body for each request.

from fastapi import FastAPI

app = FastAPI()

@app.get("/calc/{a}/{b}")
async def calc(a: int, b: int, op: str = "add"):
    return {
        "result": a + b if op == "add" else a * b
    }

# a) /calc/2/3 b) /calc/2/3?op=mul c) /calc/2/x d) /calc/2/3?op=sub



