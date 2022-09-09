
from typing import List
from ninja import Router
from backend.models import Author, Book, Genre, Items, Saved_Books
from backend.schemas import BookSchemaIn, BookSchemaOut, ItemsSchemaIn, ItemsSchemaOut, SavedBookSchemaOut

myRouters = Router()


@myRouters.post("/create_book", response=BookSchemaOut)#testing
def myFunction1(request, newBook: BookSchemaIn):
    return Book.objects.create(name=newBook.name, description=newBook.description, price=newBook.price, rate=newBook.rate, pages=newBook.pages, genre_id=newBook.genre_id, author_id=newBook.author_id, best_seller=newBook.best_seller, new_arrival=newBook.new_arrival, top_rated=newBook.top_rated, saved=newBook.saved,)


@myRouters.get("/get_all_books", response=List[BookSchemaOut])
def myFunction2(request):
    return Book.objects.all()


#when u press save or unsave button
@myRouters.get("/save_unsave_book{user_ids}/{book_ids}/{saveCondition}")
def myFunction2(request, user_ids: int, book_ids: int, saveCondition:bool):
    if(saveCondition == True):
        savedBooks = Saved_Books.objects.filter(user_id = user_ids)
        data = list(savedBooks.values())
        saved_books_ids = []
        for i in range(len(data)):
            saved_books_ids.append(data[i]['book_id'])
        if (book_ids in saved_books_ids):
            return {"msg": "Book already saved",}
        Saved_Books.objects.create(user_id= user_ids, book_id = book_ids, saved= True)
        return {"msg": "saved successfully",}
    objectss = Saved_Books.objects.filter(user_id = user_ids, book_id = book_ids)
    objectss.delete()
    return {"msg": "unsaved successfully",}

#when u press on saved
@myRouters.get("/get_all_saved_books{user_ids}", response=List[SavedBookSchemaOut])
def myFunction2(request, user_ids: int):
    return Saved_Books.objects.filter(user_id= user_ids, saved= True)


@myRouters.get("/get_all_books_by_author{author_name}", response=List[BookSchemaOut])
def myFunction3(request, author_name: str):
    return Author.objects.get(name=author_name).books.all()


@myRouters.get("/get_all_books_by_genre{genre_name}", response=List[BookSchemaOut])
def myFunction4(request, genre_name: str):
    return Genre.objects.get(name=genre_name).books.all()

# when u press on your profile
@myRouters.get("/get_all_purchased_books{user_ids}", response=List[ItemsSchemaOut])
def myFunction2(request, user_ids: int):
    return Items.objects.filter(user_id=user_ids, isBought=True)

# when u press on add to cart button
@myRouters.post("/add_to_cart")
def myFunction5(request, added_book: ItemsSchemaIn):
    Items.objects.create(
        user_id=added_book.user_id,
        book_id=added_book.book_id,
        qty=added_book.qty,
        inCart=True
    )

# when u press on the cart button
@myRouters.get("/get_personal_cart{user_ids}", response=List[ItemsSchemaOut])
def myFunction6(request, user_ids: int):
    inCart = Items.objects.filter(user_id=user_ids, inCart=True)
    return inCart

# when u press on the buy button in cart page
@myRouters.get("/Buy_items{user_ids}")
def myFunction8(request, user_ids: int):
    booksInCart = Items.objects.filter(user_id=user_ids, inCart=True)
    data = list(booksInCart.values())
    for i in range(len(data)):
        qty = (data[i]['qty'])
        objects = (Book.objects.get(id=data[i]['book_id']))
        objects.total_sales += qty
        objects.save()
        objects = booksInCart[i]
        objects.inCart = False
        objects.isBought = True
        objects.save()
    return {
        "msg": "Bought successfully",
    }

# when u press on the cart button
@myRouters.get("/get_total_items_price_and_qty{user_ids}")
def myFunction7(request, user_ids: int):

    booksInCart = Items.objects.filter(user_id=user_ids, inCart=True)
    data = list(booksInCart.values())
    totalPrice = 0
    totalqty = 0
    for i in range(len(data)):
        qty = (data[i]['qty'])
        objects = (Book.objects.get(id=data[i]['book_id']))
        totalqty += qty
        totalPrice += qty * objects.price
    return {
        "totalPrice": totalPrice,
        "totalqty": totalqty
    }

