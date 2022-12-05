from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from database.db_connect import db_connect
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

db_connect()

@app.get("/")
async def get():
    return HTMLResponse(StaticFiles())


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")