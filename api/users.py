from fastapi import APIRouter, HTTPException
from schemas.users import UserLogin, User
from crudes.users import *
from database.session import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends


router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={404: {"description": "Not found"}},
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login/", response_model=User)
async def login(user: UserLogin, db: Session = Depends(get_db)):
    db_user = get_user_by_login(db, user.login)
    if not db_user:
        raise HTTPException(status_code=401, detail="Wrong login or password")
    
    return User(**db_user.__dict__)


@router.post("/register/", response_model=User)
async def register(user: UserCreate, db: Session = Depends(get_db)):
    if not create_user(db, user):
        raise HTTPException(status_code=401, detail="Login already exists")
    return user