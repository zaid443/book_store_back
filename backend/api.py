from typing import List
from urllib import response
from ninja import Router
from backend.models import Author, Book, DesiredBook, Genre

from backend.schemas import BookSchemaIn, BookSchemaOut, DesiredBookSchema, DesiredBookSchemaOut

myRouters = Router()


@myRouters.get("/get_all_books", response=List[BookSchemaOut])
def get_all(request):
    return Book.objects.all()


@myRouters.get("/get_all_books_by_author{author_name}", response=List[BookSchemaOut])
def get_all(request, author_name: str):
    return Author.objects.get(name=author_name).books.all()


@myRouters.get("/get_all_books_by_genre{genre_name}", response=List[BookSchemaOut])
def get_all(request, genre_name: str):
    return Genre.objects.get(name=genre_name).books.all()


@myRouters.post("/bought_book")
def get_all(request, added_Book: DesiredBookSchema):
    DesiredBook.objects.create(
        user_id=added_Book.user_id,
        book_id=added_Book.book_id,
        qty=added_Book.qty,
    )


@myRouters.get("/get_cart_books", response=List[DesiredBookSchemaOut])
def get_all(request, user_ids: int):
    books = DesiredBook.objects.filter(user_id=user_ids)
    print(books)
    return books


@myRouters.post("/create", response=BookSchemaOut)
def get_all(request, newBook: BookSchemaIn):
    res = Book.objects.create(name=newBook.name,
                              description=newBook.description,
                              price=newBook.price,
                              rate=newBook.rate,
                              pages=newBook.pages,
                              genre_id=newBook.genre_id,  # take an id and choose one of the foriengkeys
                              author_id=newBook.author_id,
                              best_seller=newBook.best_seller,
                              new_arrival=newBook.new_arrival,
                              top_rated=newBook.top_rated,
                              saved=newBook.saved,
                              )
    return res

# from typing import List
# from urllib import response
# from ninja import Router
# from backend.models import Author, Book, DesiredBook, Genre

# from backend.schemas import BookSchemaIn, BookSchemaOut, DesiredBookSchema, DesiredBookSchemaOut

# myRouters = Router()


# @myRouters.get("/get_all_books", response=List[BookSchemaOut])
# def get_all(request):
#     return Book.objects.all()


# @myRouters.get("/get_all_books_by_author{author_name}", response=List[BookSchemaOut])
# def get_all(request, author_name: str):
#     return Author.objects.get(name=author_name).books.all()


# @myRouters.get("/get_all_books_by_genre{genre_name}", response=List[BookSchemaOut])
# def get_all(request, genre_name: str):
#     return Genre.objects.get(name=genre_name).books.all()


# @myRouters.post("/bought_book")
# def get_all(request, added_Book: DesiredBookSchema):
#     DesiredBook.objects.create(
#         user_id=added_Book.user_id,
#         book_id=added_Book.book_id,
#         qty=added_Book.qty,
#     )


# @myRouters.get("/get_cart_books", response=List[DesiredBookSchemaOut])
# def get_all(request, user_ids: int):
#     books = Items.objects.filter(user_id=user_ids, state)
#     print(books)
#     return books


# @myRouters.post("/create_book", response=BookSchemaOut) # testing genre_id
# def get_all(request, newBook: BookSchemaIn):
#     res = Book.objects.create(name=newBook.name,
#                               description=newBook.description,
#                               price=newBook.price,
#                               rate=newBook.rate,
#                               pages=newBook.pages,
#                               genre_id=newBook.genre_id,  
#                               author_id=newBook.author_id,
#                               best_seller=newBook.best_seller,
#                               new_arrival=newBook.new_arrival,
#                               top_rated=newBook.top_rated,
#                               saved=newBook.saved,
#                               )
#     return res
