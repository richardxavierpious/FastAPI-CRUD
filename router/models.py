from pydantic import BaseModel

class UserProfile(BaseModel):
    userid: int
    userName: str
    userBio: str

class Login(BaseModel):
    userid: int
    password: str