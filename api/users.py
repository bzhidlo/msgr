from fastapi import APIRouter
from schemas.users import User


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)

@router.post("/login", response_model=User)
async def login(user: User):
    return user

@router.post("/register")
async def register(user: User, response_model=User):
    return user