from decimal import Decimal
from ninja import Schema

# Note: some of them are useless just for testing
# image doesnt works to not used for now


class AuthorSchema(Schema):  # showed within book
    name: str


class GenreSchema(Schema):  # showed within book
    name: str


class GenresSchemaOut(Schema):  # showed in search default
    name: str
    #image: imageUrl


class AuthorsSchemaOut(Schema):  # showed in search default
    name: str
    #image: imageUrl


class BookSchema(Schema):
    name: str
    #book_image: Image.name
    description: str
    price: Decimal
    rate: Decimal
    pages: int
    language: str
    total_sales: int


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
    itemConditionInCart: bool


class SavedBookSchemaOut(Schema):
    book: BookSchema


class ItemsSchemaOut(Schema):
    book: BookSchemaOut
    qty: int
