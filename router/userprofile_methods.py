from fastapi import APIRouter
from router.db import fetch_query, execute_query
from router.models import UserProfile

get_data = APIRouter()

@get_data.post("/enterdata/{data}")
async def add_user_data(userdata: UserProfile):
    query = """
    insert into login (userid, password) values ($1, $2)
    """
    login_obj = await execute_query(query, login.userid, login.password)
    return {**login.dict(), "id": login_obj}

@get_data.get("/getdata/{id}")
async def get_login_data(user_id: int):
    query = """
    select * from login where userid = $1
    """
    result = await fetch_query(query, user_id)
    login_details = result[0]
    return {
        "userid": login_details["userid"],
        "password": login_details["password"],
    }

@get_data.put("/student/{student_id}", tags=["PUT data"])
async def update_login_data(userid: int, password: str):
    query = """
    update login set password = $1 where userid = $2 returning userid;
    """
    updated_student_id = await execute_query(query, password, userid)
    return {**userid.dict(), "id": updated_student_id}

@get_data.delete("/student/{student_id}", tags=["DELETE data"])
async def delete_student(student_id: int):
    query = """
    delete from students where id = $1 returning id;
    """
    result = await execute_query(query, student_id)
    return {"id": student_id, "message": "Student deleted successfully"}
