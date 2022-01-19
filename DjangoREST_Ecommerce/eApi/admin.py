from django.contrib import admin
from .models import import Category, Book, Product

# Register your models here.
admin.site.register(Category, Book, Product)
