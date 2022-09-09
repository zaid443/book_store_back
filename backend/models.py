from django.db import models


from django.contrib.auth import get_user_model
User = get_user_model()

# TODO: top rated, new arrival, best seller functions to set them


class Entity(models.Model):
    class Meta:
        abstract = True
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)


class Book(Entity):
    name = models.CharField('name', max_length=255)
    # maybe replaced with image URL
    book_image = models.ImageField('image', upload_to='images/', blank=True, null=True)
    # bookImageUrl = models.URLField(null= True, blank= True) # add this instead of book_image
    description = models.TextField('description', null=True, blank=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    rate = models.DecimalField('rate', blank=True, null=True, max_digits=2, decimal_places=1)
    pages = models.IntegerField('pages')
    genre = models.ForeignKey('Genre', verbose_name='genre', related_name='books',
                              on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey('Author', verbose_name='author',
                               related_name='books', null=True, blank=True, on_delete=models.SET_NULL)
    best_seller = models.BooleanField('best_seller')  # delete
    new_arrival = models.BooleanField('new_arrival')  # delete
    top_rated = models.BooleanField('top_rated')  # delete
    #saved = models.ForeignKey("SavedBooks", verbose_name=("saved"), on_delete=models.DO_NOTHING, related_name="books")
    total_sales = models.IntegerField()

    def __str__(self):
        return self.name

# class Order(Entity):
#     user = models.ForeignKey(User, verbose_name='user', related_name='orders', null=True, blank=True, on_delete=models.CASCADE)
#     totalPrice = models.IntegerField('totalPrice', blank=True, null=True) #delete!! because we have the below function
#     DesiredBook = models.ManyToManyField('DesiredBook', verbose_name='DesiredBook', related_name='orders')
#     def __str__(self):
#         return f'{self.user.first_name} + {self.totalPrice}'
# class SavedBooks(Entity):
#     user = models.ForeignKey(User, verbose_name=("user_saved_Books"), on_delete=models.DO_NOTHING)
#     #book = models.ForeignKey(Book, verbose_name=("saved_Books"), on_delete=models.DO_NOTHING, related_name="books")
#     saved = models.BooleanField('is_saved')



class Items(Entity):
    user = models.ForeignKey(User, verbose_name='user',
                             related_name='DesiredBooks', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='book',
                             on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    inCart = models.BooleanField(default=False)
    isBought = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.book.name}'

    @property
    def Items_total_price(self):
        return sum(i.book.price * i.qty for i in self.all())

    @property
    def Items_total_pieces(self):
        return sum(i.qty for i in self.filter(inCart=True, isBought=False))


class Genre(Entity):
    name = models.CharField('name', max_length=255)
    # not needed but its actually needed because of the design
    image = models.ImageField('image', upload_to='images/')
    is_active = models.BooleanField('is active')

    def __str__(self):
        return f'{self.name}'


class Author(Entity):
    name = models.CharField('name', max_length=255)

    def __str__(self):
        return f'{self.name}'
