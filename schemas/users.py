from pydantic import BaseModel
from schemas.chats import Chat
from database import models
from sqlalchemy.orm import Session

class UserBase(BaseModel):
    login: str


class UserCreate(UserBase):
    password: str
    username: str


class User(UserBase):
    id: int
    deleted: bool
    username: str
    chats: list[Chat]

    class Config:
        orm_mode = True


def create_user(db: Session, user: UserCreate):
    db_user = models.User(login=user.login, username=user.username, password=user.password)
    if not db.query(models.User).filter_by(login=user.login):
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user


def get_user_by_id(db: Session, id: int):
    db_user = db.query(models.User).filter_by(id=id).one()
    return db_user

