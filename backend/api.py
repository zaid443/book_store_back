
from typing import List
from ninja import Router
from backend.models import Author, Book, Genre, Items, Saved_Books
from backend.schemas import AuthorsSchemaOut, BookSchemaIn, BookSchemaOut, ErrorMesssage, GenresSchemaOut, ItemsSchemaIn, ItemsSchemaOut, SavedBookSchemaOut

myRouters = Router()


@myRouters.post("/create_book/", response=BookSchemaOut)#testing
def myFunction1(request, newBook: BookSchemaIn):
    return Book.objects.create(name=newBook.name, description=newBook.description, price=newBook.price, rate=newBook.rate, pages=newBook.pages, genre_id=newBook.genre_id, author_id=newBook.author_id, best_seller=newBook.best_seller, new_arrival=newBook.new_arrival, top_rated=newBook.top_rated, saved=newBook.saved,)


@myRouters.get("/get_all_books/", response=List[BookSchemaOut])
def myFunction2(request):
    return Book.objects.all()


# sort press on Authors
@myRouters.get("/get_all_authors/", response=List[AuthorsSchemaOut])
def myFunction3(request):
    return Author.objects.all()


# sort press on Genres
@myRouters.get("/get_all_genres/", response=List[GenresSchemaOut])
def myFunction4(request):
    return Genre.objects.all()


@myRouters.get("/get_all_books_by_author{author_name}/", response={200: List[BookSchemaOut], 400: ErrorMesssage})
def myFunction5(request, author_name: str):
    try:
        return Author.objects.get(name=author_name).books.all()
    except Exception:
        return 400,  {"detial": "Author Doesnt Exists"}


@myRouters.get("/get_all_books_by_genre{genre_name}/", response={200: List[BookSchemaOut], 400: ErrorMesssage})
def myFunction6(request, genre_name: str):
    try:    
        return Genre.objects.get(name=genre_name).books.all()
    except Exception:
        return 400,  {"detial": "Genre Doesnt Exists"}


#when u press save or unsave button
@myRouters.get("/save_unsave_book{user_ids}/{book_ids}/{saveCondition}/")
def myFunction7(request, user_ids: int, book_ids: int, saveCondition: bool):
    if saveCondition:
        savedBooks = Saved_Books.objects.filter(user_id=user_ids)
        data = list(savedBooks.values())
        saved_books_ids = [datum['book_id'] for datum in data]
        if book_ids in saved_books_ids:
            return {"msg": "Book already saved"}
        Saved_Books.objects.create(user_id=user_ids, book_id=book_ids, saved=True)
        return {"msg": "saved successfully"}
    objectss = Saved_Books.objects.filter(user_id=user_ids, book_id=book_ids)
    objectss.delete()
    return {"msg": "unsaved successfully"}


#when u press on saved
@myRouters.get("/get_all_saved_books{user_ids}/", response=List[SavedBookSchemaOut])
def myFunction8(request, user_ids: int):
    return Saved_Books.objects.filter(user_id= user_ids, saved= True)


# when u press on add to cart button or remove from cart
@myRouters.post("/add_remove_cart_items/")
def myFunction9(request, desiredBook: ItemsSchemaIn):
    if(desiredBook.itemConditionInCart == True):
        Items.objects.create(
            user_id=desiredBook.user_id,
            book_id=desiredBook.book_id,
            qty=desiredBook.qty,
            inCart=True
        )
        return {"msg": "Book Added Successfully",}
    objectss = Items.objects.filter(user_id = desiredBook.user_id, book_id = desiredBook.book_id, qty = desiredBook.qty)
    objectss.delete()
    return {"msg": "Book Removed Successfully",}


# when u press on the cart button
@myRouters.get("/get_personal_cart{user_ids}/", response={200:List[ItemsSchemaOut], 400: ErrorMesssage})
def myFunction10(request, user_ids: int):
    if data:= Items.objects.filter(user_id=user_ids, inCart=True):
        return data
    return 400, {"detial": "Your Cart Is Empty"}


# when u press on the cart button... and you should update it when remove item from cart 
@myRouters.get("/get_total_items_price_and_qty{user_ids}/")
def myFunction12(request, user_ids: int):
    booksInCart = Items.objects.filter(user_id=user_ids, inCart=True)
    data = list(booksInCart.values())
    totalPrice = 0
    totalqty = 0
    for datum_ in data:
        qty = datum_['qty']
        objects = Book.objects.get(id=datum_['book_id'])
        totalqty += qty
        totalPrice += qty * objects.price
    return {"totalPrice": totalPrice, "totalqty": totalqty}


# when u press on the buy button in cart page
@myRouters.get("/Buy_items{user_ids}/")
def myFunction13(request, user_ids: int):
    booksInCart = Items.objects.filter(user_id=user_ids, inCart=True)
    if data := list(booksInCart.values()):
        try:
            for i in range(len(data)):
                qty = data[i]['qty']
                objects = Book.objects.get(id=data[i]['book_id'])
                objects.total_sales += qty
                objects.save()
                objects = booksInCart[i]
                objects.inCart = False
                objects.isBought = True
                objects.save()
            return {"msg": "Items Bought successfully"}
        except Exception:
            return {"msg": "Try Again Please"}
    return {"msg": "No Books To Buy"}


# when u press on your profile
@myRouters.get("/get_all_purchased_books{user_ids}/", response=List[ItemsSchemaOut])
def myFunction14(request, user_ids: int):
    try:
        return Items.objects.filter(user_id=user_ids, isBought=True)
    except Exception:
        return{"msg": "No Purchased Books"}


# Top sales
@myRouters.get("/get_10top_sales/", response=List[BookSchemaOut])
def myFunction15(request):
    return Book.objects.order_by("total_sales").reverse()[:10]


# Top rated
@myRouters.get("/get_10top_rated/", response=List[BookSchemaOut])
def myFunction16(request):
    return Book.objects.order_by("rate").reverse()[:10]


# new arrival
@myRouters.get("/get_10top_new_arrival/", response=List[BookSchemaOut])
def myFunction17(request):
    return Book.objects.order_by("published").reverse()



