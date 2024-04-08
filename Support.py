from pydantic import BaseModel
from enum import Enum
from typing import Optional,List

class Gender(str,Enum):
    male = "male"
    female = "female"

class Role(str,Enum):
    admin = "admin"
    student = "student"
    teacher = "teacher"

class User(BaseModel):
    ID: Optional[int]
    first_name: str
    last_name:str
    middle_name: Optional[str] = None
    gender:Gender
    roles:List[Role]