from typing import List
from fastapi import FastAPI, WebSocket, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from settings.config import settings

from database.session import Base, engine
from api.users import router as users_router


def startup():
    # app
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    # router
    app.include_router(users_router)
    # mount static files
    app.mount("/static", StaticFiles(directory="static", html = True), name="static")
    # enable template engine
    templates = Jinja2Templates(directory="static")
    # middleware
    app.add_middleware(CORSMiddleware, allow_origins=settings.ORIGINS, allow_credentials=True, allow_methods=["*"], allow_headers=["*"])
    Base.metadata.create_all(bind=engine)

    return app, templates

app, templates = startup()

@app.get("/")
async def get(request : Request):
    return templates.TemplateResponse("login/template.html", {"request": request})
    
''' 
class ConnectionManager:
    def __init__(self):
        self.connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.connections.append(websocket)

    async def broadcast(self, data: str):
        for connection in self.connections:
            await connection.send_text(data)


manager = ConnectionManager()

@app.websocket("/ws/{client_id}")l
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    while True:
        data = await websocket.receive_text()
        await manager.broadcast(f"Client {client_id}: {data}")

'''