from fastapi import FastAPI,Depends,HTTPException
from database import Base,engine,get_db
from schemas import *
from sqlalchemy.orm import Session
from models import User,Post

Base.metadata.create_all(bind=engine)
app =FastAPI()

# user related routes 

@app.post("/users/", response_model=UserSchema,tags=["user"])
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    new_user = User(full_name=user.full_name)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.get("/users/{user_id}", response_model=UserSchema,tags=["user"])
async def get_user_and_all_posts(user_id: int, db: Session = Depends(get_db)):
    result = db.query(User).where(User.id == user_id)
    if not result:
        raise HTTPException(status_code=404, detail="User not found")
    return result

@app.post("/posts",response_model=PostSchema,tags=["post"])
def create_post(owner_id:int,post:PostCreate,db: Session = Depends(get_db)):
    new_post=Post(title=post.title,description=post.description,owner_id=owner_id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get("/posts/{post_id}", response_model=PostSchema, tags=["post"])
def read_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@app.put("/posts/{post_id}", response_model=PostSchema, tags=["post"])
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    existing_post = db.query(Post).filter(Post.id == post_id).first()
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")

    existing_post.title = post.title or existing_post.title
    existing_post.description = post.description or  existing_post.description
    db.commit()
    db.refresh(existing_post)
    return existing_post

@app.delete("/posts/{post_id}", tags=["post"])
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(post)
    db.commit()
    return {"message":"delete Post Successfully"}
