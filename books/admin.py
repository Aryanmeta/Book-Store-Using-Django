from django.contrib import admin
from .models import Book, Comment


@admin.register(Book)
class Book(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'cover', )


@admin.register(Comment)
class Comment(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_created', )
