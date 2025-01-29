from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_ola_mundo():
    client = TestClient(app)  # Arrange ambiente e cliente para testes

    response = client.get('/api/v1')  # Act executa a requisição

    assert response.status_code == HTTPStatus.OK  # Assert verifica o resultado
    assert response.json() == {'message': 'Olá, Mundo!'}
