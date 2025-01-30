from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from fast_zero.home import home
from fast_zero.schemas import Message, UserDb, UserList, UserPublic, UserSchema

app = FastAPI()

database = []  # fake database

# Monta o aplicativo home na raiz /
app.include_router(home)


# Endpoint /api/v1
@app.get('/api/v1', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá, Mundo!'}


# Endpoint para criar usuários /api/v1/users
@app.post(
    '/api/v1/users', status_code=HTTPStatus.CREATED, response_model=UserPublic
)
def create_user(user: UserSchema):
    user_with_id = UserDb(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)

    return user_with_id

# Busca lista de usuarios
@app.get('/api/v1/users', response_model=UserList)
def read_users():
    return {'users': database}

# Atualiza um usuario pelo id
@app.put('/api/v1/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: UserSchema):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado',
        )

    user_with_id = UserDb(id=user_id, **user.model_dump())
    database[user_id - 1] = user_with_id
    return user_with_id

# Busca um usuario pelo id
@app.get('/api/v1/user/{user_id}', response_model=UserPublic)
def read_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado',
        )

    return database[user_id - 1]

# Deleta um usuario pelo id
@app.delete('/api/v1/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='Usuário não encontrado',
        )

    del database[user_id - 1]
    return {'message': 'Usuário deletado com sucesso'}
