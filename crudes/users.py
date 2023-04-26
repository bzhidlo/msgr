from database import models
from sqlalchemy.orm import Session
from schemas.users import UserCreate

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