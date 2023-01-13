from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import cx_Oracle
from database.config import host, port, sid

import sys
import os

def db_connect():
    cx_Oracle.init_oracle_client(lib_dir= r"D:/oracle/instantclient_21_7")

    preq = cx_Oracle.makedsn(host, port, sid=sid)

    con_string = 'oracle://{user}:{pwd}@{preq}'

    engine = create_engine(
        con_string,
        convert_unicode=False,
        pool_recycle=10,
        pool_size=50,
        echo=True
    )

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    Base = declarative_base()

    Base.metadata.create_all(bind=engine)
