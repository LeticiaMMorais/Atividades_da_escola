'''
Docstring for fast_car_api.models
'''
'''
Aqui vamos criar as tabelas do banco de dados.
'''

from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    message: str

#Essa é a classe que vai basear a entrada da API para o banco de dados
class CarSchema(BaseModel): 
    brand: str
    model: str
    color: Optional[str] = None
    factory_year: Optional[int] = None
    model_year: Optional[int] = None
    description: Optional[str] = None

#Essa é a classe para retornar os dados presentes no banco:
class CarPublic(BaseModel):
    id: int
    brand: str
    model: str
    color: Optional[str]
    factory_year: Optional[int]
    model_year: Optional[int]
    description: Optional[str]
