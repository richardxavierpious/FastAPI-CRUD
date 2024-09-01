import asyncpg
from typing import Optional
from models import session, Login2

DATABASE_URL = "postgresql://postgres:admin@localhost/InBytes"

async def get_connection():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn


async def execute_query(query: str, *args):
    conn = await get_connection()
    try:
        await conn.execute(query, *args)
    finally:
        await conn.close()


async def fetch_query(query: str, *args):
    conn = await get_connection()
    try:
        result = await conn.fetch(query, *args)
        return result
    finally:
        await conn.close()