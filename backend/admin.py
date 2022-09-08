from django.contrib import admin

from .models import Book, Order, Author, DesiredBook, Genre 

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'pages', 'genre', 'author', 'top_rated']

class DesiredBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'qty','user']

class OrdersAdmin(admin.ModelAdmin):
    list_display = ['totalPrice', 'status', 'user']

class GenreAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id',  'name']

admin.site.register(Book, BookAdmin)
admin.site.register(DesiredBook, DesiredBookAdmin )
admin.site.register(Order, OrdersAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Genre, GenreAdmin)






    # list_filter = ('',)
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
