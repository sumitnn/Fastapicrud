from pydantic import BaseModel
from typing import List,Optional
class UserBase(BaseModel):
    full_name:str

class UserCreate(UserBase):
    pass

class UserSchema(UserBase):
    id:int
    posts:List['PostSchema']


# post related 

class PostBase(BaseModel):
    title:str
    description:str

class PostCreate(PostBase):
    pass
    
class PostUpdate(BaseModel):
    title:Optional[str]
    description:Optional[str]

class PostSchema(PostBase):
    id:int


    
