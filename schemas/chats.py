from pydantic import BaseModel


class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass


class Chat(ChatCreate):
    id: int

    class Config:
        orm_mode = True