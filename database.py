from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql

# Check if the database exists, and create it if not
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='', 
)

cursor = connection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS crud_db")
connection.close()


SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:@localhost:3306/crud_db'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()