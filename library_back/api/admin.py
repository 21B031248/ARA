from django.contrib import admin

from api.models import Category, Book, Favorite

admin.site.register(Category)
admin.site.register(Book)
admin.site.register(Favorite)
