from flask import redirect
from library import app, db, home_tag, book_tag
from models.models import Books
from schemas import BookSchema, ErrorSchema, show_books
from schemas.books import BookViewSchema, BookSearchSchema
from sqlalchemy.exc import IntegrityError
from urllib.parse import unquote


@app.get('/', tags=[home_tag])
def home():
    """
    Redireciona para openapi
    """
    return redirect('/openapi')


@app.get('/livros', tags=[book_tag], responses={"200": BookSchema, "404": ErrorSchema})
def index():
    """
    Busca e retorna todos os livros cadastrados
    """
    books = db.session.query(Books).all()
    return show_books(books), 200


@app.post('/criar', tags=[book_tag], responses={"200": BookViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def criar(form: BookSchema):
    """
    Adiciona um novo livro ao bando de dados
    """

    new_book = Books(
        name=form.name,
        category=form.category,
        author=form.author
    )

    try:
        db.session.add(new_book)
        db.session.commit()
        return show_books(new_book), 200

    except IntegrityError as e:
        error_message = "Livro já está cadastrado!"
        return {"message": error_message}, 409

    except Exception as e:
        error_message = "Não foi possível salvar o livro"
        return {"message": error_message}, 400


@app.post('/atualizar', tags=[book_tag], responses={"200": BookViewSchema, "409": ErrorSchema, "400": ErrorSchema})
def atualizar(form: BookSchema):
    """
    Adiciona o livro alterado ao bando de dados
    """
    book_update = db.session.query(Books).filter(Books.id == form.id)
    book_update.update(
        {
            'id': form.id,
            "name": form.name,
            "category": form.category,
            "author": form.author
        }
    )
    db.session.commit()

    if book_update:
        return {"message": "Livro atualizado"}, 200
    else:
        error_msg = "Livro não encontrado"
        return {"mesage": error_msg}, 404


@app.delete('/deletar', tags=[book_tag], responses={"200": BookSchema, "404": ErrorSchema})
def deletar(query: BookSearchSchema):
    """
    Deleta um livro do bando de dados
    """
    book_name = unquote(unquote(query.name))
    print(book_name)
    count = db.session.query(Books).filter(Books.name == book_name).delete()
    db.session.commit()

    if count:
        return {"message": "Livro removido", "id": book_name}
    else:
        error_msg = "Livro não encontrado"
        return {"mesage": error_msg}, 404
