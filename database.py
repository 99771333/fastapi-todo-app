from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL,connect_args={"check_same_thread": False}) #engine mtlb database se connection establish krne k liye use hota hai

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #SessionLocal mtlb database se session create krne k liye use hota hai, jisse hum apne database operations perform kr sakte hain.

Base = declarative_base() #Base mtlb database ke tables ko define krne k liye use hota hai, jisse hum apne models.py file me apne tables ko define kr sakte hain.
