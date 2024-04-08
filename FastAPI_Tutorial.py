from fastapi import FastAPI,HTTPException
from Support import User,Gender,Role
from typing import List

app = FastAPI()

database : List[User] = [
    User(
        ID = 123,
        first_name = "Pagalavan ",
        last_name = "Manoharan",
        middle_name = "Temp",
        gender = Gender.male,
        roles = [Role.student]
    )
]

@app.get("/")
async def root():
    return {"HI":123}

@app.get("/get_values")
async def func():
    return database

@app.post("/post_user")
async def post(user : User):
    database.append(user)
    return {"ID" : user.ID}

@app.delete("/delete_user/{user_id}")
async def delete(user_id: int):
    for i in database:
        if(i.ID == user_id):
            database.remove(i)
            return {"REMOVED" : user_id}
    raise HTTPException(
        status_code=404,
        detail=f"User with {user_id} does not exists"
    )