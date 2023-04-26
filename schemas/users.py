from pydantic import BaseModel


class UserBase(BaseModel):
    login: str


class UserLogin(UserBase):
    password: str


class UserCreate(UserLogin):
    username: str


class User(UserLogin):
    id: int
    deleted: bool
    username: str

    class Config:
        orm_mode = True