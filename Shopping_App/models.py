from django.db import models

# Create your models here.
# models.py

from django.db import models

class Product(models.Model):
    shape = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'Shopping_App'

class User(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    address = models.TextField()
    class Meta:
        app_label = 'Shopping_App'

class Recommendation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    class Meta:
        app_label = 'Shopping_App'