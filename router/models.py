from pydantic import BaseModel

class StudentData(BaseModel):
    name: str
    age: int
    grade: str

class UserProfile(BaseModel):
    userId: int
    userName: str
    userBio: str

class Login(BaseModel):
    userId: int
    password: int