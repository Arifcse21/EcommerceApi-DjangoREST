from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    isbn = models.CharField(max_length=13)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.IntegerField()
    description = models.TextField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.title

class Product(models.Model):
    product_tag = models.CharField(max_length=15)
    name = models.CharField(max_length=15)
    category = models.ForeignKey(Category,related_name='products', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9,decimal_places=2)
    stock = models.IntegerField()
    image_url = models.URLField()
    status = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return f"{self.product_tag} {self.name}"
