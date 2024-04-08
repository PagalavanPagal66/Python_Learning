from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import Annotated
import Models
from Database import engine,SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()
Models.Base.metadata.create_all(bind=engine)

class Postbase(BaseModel):
    title : str
    content : str
    user_id : int

class Userbase(BaseModel):
    username : str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session,Depends(get_db)]

@app.post("/put_user/",status_code=status.HTTP_201_CREATED)
def put_user(db:db_dependency,user : Userbase):
    db_user = Models.User(**user.dict())
    db.add(db_user)
    db.commit()

@app.post("/put_post/",status_code=status.HTTP_201_CREATED)
def put_post(db:db_dependency,post : Postbase):
    db_post = Models.Post(**post.dict())
    db.add(db_post)
    db.commit()


@app.get("/")
def home():
    return {"Hi","hello"}

@app.get("/get_user/",status_code=status.HTTP_200_OK)
def get_user(user_id:int,db:db_dependency):
    user = db.query(Models.User).filter(Models.User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@app.get("/get_post/",status_code=status.HTTP_200_OK)
def get_post(post_id : int,db:db_dependency):
    post = db.query(Models.Post).filter(Models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404,detail= "Post not found")
    return post

@app.delete("/delete_post/",status_code=status.HTTP_200_OK)
def del_post(post_id : int,db:db_dependency):
    post = db.query(Models.Post).filter(Models.Post.id == post_id).first()
    if post is None:
        raise HTTPException(status_code=404,detail = "Post not found")
    db.delete(post)
    db.commit()
    return {"Deleted" : post}