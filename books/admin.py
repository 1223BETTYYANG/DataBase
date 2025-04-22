from django.contrib import admin
from .models import *
from django.db import connection


# Register your models here.
class BooksInfoAdmin(admin.ModelAdmin):
    list_per_pag = 15
    list_display = ['id', 'title', 'type', 'picture', 'price', 'address', 'description']
    list_filter = ['title']
    search_fields = ['title']


admin.site.register(BooksInfo, BooksInfoAdmin)


