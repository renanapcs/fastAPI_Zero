from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.home import home


def test_root_deve_retornar_ola_mundo_em_html():
    client = TestClient(home)

    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert '<h1> Olá Mundo </h1>' in response.text
