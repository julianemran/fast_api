from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

class Password(BaseModel):
    password: str
        
