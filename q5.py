from fastapi import FastAPI

app = FastAPI()

@app.get("/flag")
async def flag(on: bool = False):
    return {"on": on}
    return {"on": on}


