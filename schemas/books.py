from pydantic import BaseModel
from models.models import Books
from typing import Optional, List


class BookSchema(BaseModel):
    """ Define como um novo produto a ser inserido deve ser representado
    """
    name: str = "Harry Potter"
    category: str = "Fantasia"
    author: str = "J.K Rowling"


def show_books(booklist: List[Books]):
    """ Retorna uma representação do produto seguindo o schema definido em
        BookViewSchema.
    """

    result = []
    for book in booklist:
        result.append({
            "name": book.name,
            "category": book.category,
            "author": book.author
        })

    return {"books": result}
