from fastapi import FastAPI
from models import User, Password

app = FastAPI()

users_map = {"1": {"name": "John Doe", "age": 25}, "2": {"name": "Elizabeth Windsor", "age": 90}}
secret_pass = "1234"

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def get_users():
    return users_map

@app.get("/user/{id}")
async def get_specific_user(id):
    return users_map[id] if id in users_map else {"message": "Not found", "code": 404}

@app.post("/users/{id}")
async def add_user(details: User, id):
    users_map[id] = details
    return {"message": "Added user successfully", "code": 200}

@app.delete("/users/{id}")
async def remove_user(password: Password, id):
    if password.password == secret_pass:
        if id in users_map:
            del users_map[id]
            return {"message": "deleted successfully", "code": 200}
        else:
            return {"message": "Not found", "code": 404}
    else:
        return {"message": "Not authorized", "code": 403}