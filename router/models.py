from pydantic import BaseModel

class StudentData(BaseModel):
    name: str
    age: int
    grade: str
