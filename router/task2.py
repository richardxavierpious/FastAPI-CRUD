from fastapi import APIRouter

from router.db import execute_query
from router.models import StudentData

get_data = APIRouter()

@get_data.post("/enterdata/{number}")
async def add_student(student: StudentData):
    query = """
    insert into students (name, age, grade) values ($1, $2, $3)
    """
    student_id = await execute_query(query, student.name, student.age, student.grade)
    return {**student.dict(), "id": student_id}
