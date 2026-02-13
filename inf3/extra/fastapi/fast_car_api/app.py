from fastapi import FastAPI

from fast_car_api.routers import router as car_router

app = FastAPI(
    title="Fast Car API",
    description='Um projeto para aprendizagem de FastAPI.',
    version='0.0.1'
)

app.include_router(car_router) # Dizendo para incluir a rota que declaramos com uma rota da aplicação

# Rota da API para realizar alguma função
@app.get('/') # Essa é  rota Raiz (root)
def read_root():
    return {'Amante de carros': 'Pode dar uma olhada nos nossos carros'}