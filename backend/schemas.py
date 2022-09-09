from decimal import Decimal
from ninja import Schema

# Note: some of them are useless just for testing
# image doesnt works to not used for now


class AuthorSchema(Schema):
    name: str


class GenreSchema(Schema):
    name: str
    # image: Image. 
    is_active: bool


class BookSchema(Schema):
    name: str
    #book_image: Image.name
    description: str
    price: Decimal
    rate: Decimal
    pages: int
    


class BookSchemaOut(BookSchema):
    id: int
    genre: GenreSchema
    author: AuthorSchema


class BookSchemaIn(BookSchema):  # testing
    genre_id: int
    author_id: int


class ItemsSchemaIn(Schema):
    user_id: int
    book_id: int
    qty: int
    inCart: bool

class SavedBookSchemaOut(Schema):
    book: BookSchema

class ItemsSchemaOut(Schema):
    book: BookSchemaOut
    qty: int
