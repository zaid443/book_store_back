from decimal import Decimal
from ninja import Schema

# Note: some of them are useless just for testing


class AuthorSchema(Schema):
    name: str


class GenreSchema(Schema):
    name: str
    # image: Image. #not needed
    is_active: bool


class BookSchema(Schema):
    name: str
    #book_image: Image.name
    description: str
    price: Decimal
    rate: Decimal
    pages: int
    best_seller: bool
    new_arrival: bool
    top_rated: bool
    saved: bool


class BookSchemaOut(BookSchema):
    id: int
    genre: GenreSchema
    author: AuthorSchema


class BookSchemaIn(BookSchema):  # testing 
    genre_id: int
    author_id: int


class DesiredBookSchema(Schema):
    user_id: int
    book_id: int
    qty: int


class DesiredBookSchemaOut(Schema):
    user_id: int
    book: BookSchemaOut
    qty: int
