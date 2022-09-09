from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# TODO: images Users
class Entity(models.Model):
    class Meta:
        abstract = True
    published = models.DateField(editable=True, verbose_name='Published Data')
    created = models.DateTimeField(editable=False, auto_now_add=True)
    updated = models.DateTimeField(editable=False, auto_now=True)


class Book(Entity):
    name = models.CharField('name', max_length=255)
    book_image = models.ImageField('image', upload_to='images/', blank=True, null=True) # maybe replaced with image URL
  # bookImageUrl = models.URLField(null= True, blank= True) # add this instead of book_image
    description = models.TextField('description', null=True, blank=True)
    price = models.DecimalField('price', max_digits=10, decimal_places=2)
    rate = models.DecimalField('rate', blank=True, null=True, max_digits=2, decimal_places=1)
    pages = models.IntegerField('pages')
    total_sales = models.IntegerField()
    genre = models.ForeignKey('Genre', verbose_name='genre', related_name='books', on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey('Author', verbose_name='author', related_name='books', null=True, blank=True, on_delete=models.SET_NULL)
    savedBooks = models.ManyToManyField("Saved_Books", verbose_name=("savedbook"),related_name="books", blank=True, null=True)
    language = models.CharField('Language',max_length=10,choices=[
        ('Arabic','Arabic'),
        ('English','English'),
    ])
    def __str__(self):
        return self.name

class Saved_Books(models.Model):
    user = models.ForeignKey(User, verbose_name=("user_saved_Books"), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name=("saved_Books"), on_delete=models.CASCADE, related_name='here')
    saved = models.BooleanField('isSaved')
    def __str__(self):
        return self.book.name
    
class Items(models.Model):
    user = models.ForeignKey(User, verbose_name='user', related_name='DesiredBooks', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, verbose_name='book', on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)
    inCart = models.BooleanField(default=False)
    isBought = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.book.name}'

class Genre(models.Model):
    name = models.CharField('name', max_length=255)
    image = models.ImageField('image', upload_to='images/') # not needed but its actually needed because of the design
    is_active = models.BooleanField('is active')
    def __str__(self):
        return f'{self.name}'

class Author(models.Model):
    name = models.CharField('name', max_length=255)
    image = models.ImageField('image', upload_to='images/') # not needed but its actually needed because of the design
    is_active = models.BooleanField('is active')
    def __str__(self):
        return f'{self.name}'
