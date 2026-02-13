import asyncpg
from fastapi import FastAPI

app = FastAPI()

async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="your-password",
        database="your-database",
        host="localhost"
    )

@app.get("/")
async def test_connection():
    conn = await get_db_connection()
    await conn.close()
    return {"message":"Conexão com o PostgreSQL bem-sucedida!"}

@app.get("/data")
async def get_dados():
    conn = await get_db_connection()
    rows = await conn.fetch("SELECT * FROM ")
    await conn.close()

    return {}