from pydantic import BaseModel
from datetime import datetime

class MessageBase(BaseModel):
    body: str


class MessageCreate(MessageBase):
    user_id: int
    chat_id: int


class Message(MessageCreate):
    id: int
    created_at: datetime
    updated_at: datetime
    read: bool

    class Config:
        orm_mode = True