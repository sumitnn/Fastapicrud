from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    full_name=Column(String(30),nullable=False,unique=True)
    posts=relationship('Post',back_populates="owner")


class Post(Base):
    __tablename__="posts"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50))
    description=Column(Text)
    owner_id=Column(Integer,ForeignKey("users.id"))
    owner=relationship('User',back_populates="posts")

