from sqlalchemy import Boolean , Integer , String , Column
from Database import Base

class User(Base):
    __tablename__ = 'users_new'

    id = Column(Integer,primary_key=True,index=True)
    username = Column(String(15),unique=True)


class Post(Base):
    __tablename__ = 'posts_new'

    id = Column(Integer,primary_key=True,index=True)
    title = Column(String(25))
    content = Column(String(50))
    user_id = Column(Integer)
