from http import HTTPStatus

from fastapi import FastAPI

from fast_zero.home import home
from fast_zero.schemas import Message

app = FastAPI()


# Endpoint /api/v1
@app.get('/api/v1', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


# Monta o aplicativo home na raiz
app.mount('/', home)
