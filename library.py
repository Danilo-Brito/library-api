from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from routes import routes
from flask_openapi3 import Tag, OpenAPI
from flask_cors import CORS

app = OpenAPI(__name__)
app.config.from_pyfile('config.py')
CORS(app)

db = SQLAlchemy(app)

if __name__ == '__main__':
    routes.app.run(debug=True)

home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
book_tag = Tag(name="Livros", description="Adição, visualização e remoção dos livros da base")
