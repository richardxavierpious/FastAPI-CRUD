from fastapi import APIRouter
from router.db import fetch_query, execute_query
from router.models import StudentData

get_data = APIRouter()

@get_data.post("/enterdata/{data}")
async def add_student(student: StudentData):
    query = """
    insert into students (name, age, grade) values ($1, $2, $3)
    """
    student_id = await execute_query(query, student.name, student.age, student.grade)
    return {**student.dict(), "id": student_id}

@get_data.get("/getdata/{id}")
async def get_student(student_id: int):
    query = """
    select * from students where id = $1
    """
    result = await fetch_query(query, student_id)
    student_record = result[0]
    return {
        "id": student_record["id"],
        "name": student_record["name"],
        "age": student_record["age"],
        "grade": student_record["grade"]
    }

@get_data.put("/student/{student_id}", tags=["PUT data"])
async def update_student(student_id: int, student: StudentData):
    query = """
    update students set name = $1, age = $2, grade = $3 where id = $4 returning id;
    """
    updated_student_id = await execute_query(query, student.name, student.age, student.grade, student_id)
    return {**student.dict(), "id": updated_student_id}

@get_data.delete("/student/{student_id}", tags=["DELETE data"])
async def delete_student(student_id: int):
    query = """
    delete from students where id = $1 returning id;
    """
    result = await execute_query(query, student_id)
    return {"id": student_id, "message": "Student deleted successfully"}
