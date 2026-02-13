'''
Docstring for fast_car_api.database
'''
'''
Nesse arquivo vão ficar as configurações com o banco de dados e sua conexão
'''
import asyncpg

async def get_db_connection():
    return await asyncpg.connect(
        user="postgres",
        password="your-password",
        database="your-database",
        host="localhost",
        port="5432"
    )