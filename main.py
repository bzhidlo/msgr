from fastapi import FastAPI
from database.db_connect import db_connect

app = FastAPI()

db_init()

@app.get("/")
async def root():
    return {"message": "Hello World"}