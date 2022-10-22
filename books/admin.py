from django.contrib import admin
from .models import Book


# @admin.register(Book)
# class Book(admin.ModelAdmin):
#     list_display = ('title', 'author', 'price', )


admin.site.register(Book)