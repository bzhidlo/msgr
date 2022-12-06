from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import cx_Oracle

def db_connect():
    # pre-requisits for connection
    host='localhost'
    port=1521
    sid='orcl'
    user='c##sqlserverguides'
    pwd='root'

    preq = cx_Oracle.makedsn(host, port, sid=sid)

    # connection string
    con_string = 'oracle://{user}:{pwd}@{preq}'

    # using SQLAlchemy to create connection
    engine = create_engine(
        con_string,
        convert_unicode=False,
        pool_recycle=10,
        pool_size=50,
        echo=True
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()