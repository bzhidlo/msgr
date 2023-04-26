from pydantic import BaseModel
from schemas.messages import Message

class ChatBase(BaseModel):
    name: str


class ChatCreate(ChatBase):
    pass


class Chat(ChatCreate):
    id: int
    messages: list[Message]


    class Config:
        orm_mode = True