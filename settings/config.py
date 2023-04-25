import os

class Settings:
    # main
    PROJECT_NAME:str = "Websocket chat"
    PROJECT_VERSION: str = "1.0.0"

    #database
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./database.db"

    #middleware
    ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    ]

settings = Settings()