from fastapi import APIRouter
from db import fetch_query, execute_query
from models import Login, Login2, session

get_data = APIRouter()

@get_data.post("/enterdata/{data}")
async def add_login_data(login: Login):
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

@get_data.put("/student/{userid}", tags=["PUT data"])
async def update_login_data(userid: int, password: str):
    query = """
    update login set password = $1 where userid = $2 returning userid;
    """
    updated_user_id = await execute_query(query, password, userid)
    return {"userid": userid, "updated_user_id": updated_user_id}

@get_data.delete("/student/{student_id}", tags=["DELETE data"])
async def delete_student(student_id: int):
    query = """
    delete from login where userid = $1 returning userid;
    """
    result = await execute_query(query, student_id)
    return {"userid": student_id, "message": "User deleted successfully"}

@get_data.post("/enterdataorm/{data}")
async def add_login(text: str, is_complete: bool = False):
    login_obj = Login2(text=text, is_done=is_complete)
    session.add(login_obj)
    session.commit()
    return {"todo added": login_obj.text}
