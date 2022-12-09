from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login")
async def login():
    return [{'logined' : 'yes'}]