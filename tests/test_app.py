from http import HTTPStatus


def test_root_deve_retornar_ok_ola_mundo(client):
    response = client.get('/api/v1')  # Act executa a requisição

    assert response.status_code == HTTPStatus.OK  # Assert verifica o resultado
    assert response.json() == {'message': 'Olá, Mundo!'}


def test_create_user(client):
    response = client.post(
        '/api/v1/users',
        json={
            'username': 'fula',
            'email': 'fula@exa.com',
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'fula',
        'email': 'fula@exa.com',
        'id': 1,
    }


def test_read_users(client):
    response = client.get('/api/v1/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'fula',
                'email': 'fula@exa.com',
                'id': 1,
            }
        ]
    }


def test_read_user(client):
    response = client.get('/api/v1/user/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'fula',
        'email': 'fula@exa.com',
        'id': 1,
    }


def test_read_user_not_found(client):
    response = client.get('/api/v1/user/2')

    assert response.status_code in {
        HTTPStatus.NOT_FOUND,
        HTTPStatus.UNPROCESSABLE_ENTITY,
    }
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_update_user(client):
    response = client.put(
        '/api/v1/users/1',
        json={
            'username': 'fula',
            'email': 'fula@exa.com',
            'id': 1,
            'password': '123456',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'fula',
        'email': 'fula@exa.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/api/v1/users/2',
        json={
            'username': 'fula',
            'email': 'fula@exa.com',
            'password': '123456',
            'id': 2,
        },
    )

    assert response.status_code in {
        HTTPStatus.NOT_FOUND,
        HTTPStatus.UNPROCESSABLE_ENTITY,
    }
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_user(client):
    response = client.delete('/api/v1/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Usuário deletado com sucesso'}


def test_delete_user_not_found(client):
    response = client.delete('/api/v1/users/2')

    assert response.status_code in {
        HTTPStatus.NOT_FOUND,
        HTTPStatus.UNPROCESSABLE_ENTITY,
    }
    assert response.json() == {'detail': 'Usuário não encontrado'}
