from pydantic import BaseModel
from models.models import Books
from typing import List


class BookSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    id: int = 1
    name: str = "Harry Potter"
    category: str = "Fantasia"
    author: str = "J.K Rowling"


class BookViewSchema(BaseModel):
    id: int = 1
    name: str = "Harry Potter"
    category: str = "Fantasia"
    author: str = "J.K Rowling"


class BookSearchSchema(BaseModel):
    """ Retorna uma representação do produto seguindo o schema definido em
        BookViewSchema.
    """
    name: str = "Harry Potter"


def show_books(booklist: List[Books]):
    """ Retorna uma representação do produto seguindo o schema definido em
        BookViewSchema.
    """

    result = []
    for book in booklist:
        result.append({
            "id": book.id,
            "name": book.name,
            "category": book.category,
            "author": book.author
        })

    return {"books": result}
