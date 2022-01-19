from rest_framework import serializers
from .models import Category, Book, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields =['id','title']
        model = Category

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        fields =['id', 'title','author', 'category', 'isbn', 
        'price', 'stock', 'description', 'status', 'date_created']
        model = Book

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id','product_tag', 'name','category','price',
        'stock','image_url','status','date_created']