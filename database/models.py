from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Text, Table
from sqlalchemy.orm import relationship
from sqlalchemy import func

from database.session import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, index=True)
    password = Column(String)
    username = Column(String)
    deleted = Column(Boolean, default=False)

    messages = relationship("Message", back_populates='sender')
    chats = relationship("Chat", secondary='chats_to_users', back_populates='members')

    def __repr__(self):
        return f'<Post "{self.username}">'


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    chat_id = Column(Integer, ForeignKey("chats.id"))
    body = Column(Text)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())
    read = Column(Boolean, default=False)

    sender = relationship("User", back_populates='messages')

    def __repr__(self):
        return f'<Post "{self.body}">'


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    members = relationship("User", secondary='chats_to_users', back_populates='chats')

    def __repr__(self):
        return f'<Post "{self.name}">'


chats_to_users = Table('chats_to_users',
                    Base.metadata,
                    Column('user_id', Integer, ForeignKey('users.id')),
                    Column('chat_id', Integer, ForeignKey('chats.id'))
                )   
