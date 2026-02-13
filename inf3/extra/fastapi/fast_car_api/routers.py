from fastapi import APIRouter, HTTPException, status
import asyncpg

from fast_car_api.database import get_db_connection
from fast_car_api.models import (
     CarPublic,
     CarSchema,
     Message
)

'''
O APIRouter declara a rota junto do controler/view...

O conjunto da URL com a função que é executada nela se chama "router" ("rota" em português).
'''

router = APIRouter(
    prefix='/api/v1/cars',
    tags=['cars']
)

'''
O APIRouter() serve para criar uma rota com algumas configurações.

Mas só definir aqui não é o suficiente, tem que importar no arquivo em que est
'''

# É boa prática colocar um prefixo.

@router.post(
    path='/create_car',
    response_model=Message,
    status_code=status.HTTP_201_CREATED
)
async def create_car(car: CarSchema):
    conn = await get_db_connection()
    await conn.execute('INSERT INTO car(brand, model, color, factory_year, model_year, description) VALUES ($1,$2,$3,$4,$5,$6)', car.brand, car.model, car.color, car.factory_year, car.model_year, car.description)
    await conn.close()
    return {'message': f'O carro {car.model} foi adicionado com sucesso'}


@router.get(
    path='/list_cars',
    status_code=status.HTTP_200_OK
)
async def list_car():
    conn = await get_db_connection()
    cars = await conn.fetch("SELECT car.id, car.brand, car.model, car.factory_year, car.model_year, car.description FROM car")
    print(cars)
    print(type(cars))
    await conn.close()

    list_of_cars = []
    for car in cars:
        list_of_cars.append({'id':f'{car["id"]}', 'brand':f'{car["brand"]}', 'model':f'{car["model"]}', 'factory_year':f'{car["factory_year"]}', 'model_year':f'{car["model_year"]}', 'description':f'{car["description"]}'})
    return {'Carros Cadastrados': list_of_cars}

@router.get(
    path='/{car_id}',
    status_code=status.HTTP_200_OK
)
async def get_car(car_id: int):
    conn = await get_db_connection()

    car_item = await conn.fetch('SELECT car.id, car.brand, car.model, car.factory_year, car.model_year, car.description FROM car WHERE car.id = $1;', car_id)

    await conn.close()

    if not car_item:
        raise HTTPException (
            status_code=status.HTTP_404_NOT_FOUND,
            detail ='Car not found'
        )
    
    return car_item


@router.delete(
    path='/delete/{car_id}',
    status_code=status.HTTP_200_OK
)
async def delete_car(car_id: int):
    conn = await get_db_connection()

    car_del = await conn.fetch('SELECT * FROM car WHERE car.id = $1', car_id)
    if not car_del:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Car with id {car_id} not found'
        )
    else:
        await conn.execute('DELETE FROM car WHERE car.id = $1', car_id)
    await conn.close()
    return {"message":"car with id {} was deleted successfully".format(car_id)}