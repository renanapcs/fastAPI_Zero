from fastapi import APIRouter
from fastapi.responses import HTMLResponse

home = APIRouter()


@home.get('/', response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>"""
