from database import models
from sqlalchemy.orm import Session
from schemas.users import UserCreate
from sqlalchemy import exc


def create_user(db: Session, user: UserCreate):
    db_user = models.User(login=user.login, username=user.username, password=user.password)
    try: 
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except exc.SQLAlchemyError:
        return None
    
    return db_user


def get_user_by_id(db: Session, id: int):
    try:
        db_user = db.query(models.User).filter_by(id=id).one()
    except exc.SQLAlchemyError:
        return None
        
    return db_user


def get_user_by_login(db: Session, login: str):
    try:
        db_user = db.query(models.User).filter_by(login=login).one()
    except exc.SQLAlchemyError:
        return None
    
    return db_user