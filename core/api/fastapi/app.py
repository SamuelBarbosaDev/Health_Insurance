import pickle
import uvicorn
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel


# Iniciando a API:
app = FastAPI()


# Carregando modelo:
path = r'core/models/model.pkl'

with open(path, 'rb') as file:
    model = pickle.load(file)


# Criando a página inicial:
@app.get('/')
def home():
    return 'Welcome to the medical Insurance Prediction API'


@app.get('/predict')
def predict(age: int, bmi: float, children: int, smoker: str = 'no'):
    df_input = pd.DataFrame([dict(age=age, bmi=bmi, children=children, smoker=smoker)])
    output = model.predict(df_input)[0]
    return output


# Classifica sobrevivência (consumo do modelo) com input no formato Json
class Customer(BaseModel):
    age: int
    bmi: float
    children: int
    smoker: str

    # Exemplo de uso:
    class Config:
        json_schema_extra = {
            "example": {
                "age": 20,
                "bmi": 30.4,
                "children": 1,
                "smoker": "no",
            }
        }


@app.post('/predict_with_json')
def predict_with_json(data: Customer):
    df_input = pd.DataFrame([data.model_dump()])
    output = model.predict(df_input)[0]
    return output


# Classifica sobrevivência (consumo do modelo) com input no formato Json - lista
class CustomerList(BaseModel):
    data: List[Customer]


@app.post('/mult_predict_with_json')
def mult_predict_with_json(data: CustomerList):
    df_input = pd.DataFrame(data.model_dump()['data'])
    output = model.predict(df_input).tolist()
    return output


if __name__ == '__main__':
    uvicorn.run(app)
