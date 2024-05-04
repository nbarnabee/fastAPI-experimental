import httpx

from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
async def hello():
    return {"Hello": "World"}
