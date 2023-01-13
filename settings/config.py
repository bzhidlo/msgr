class Settings:
    PROJECT_NAME:str = "Websocket chat"
    PROJECT_VERSION: str = "1.0.0"
    #middleware
    ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    ]

settings = Settings()