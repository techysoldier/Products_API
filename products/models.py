from django.db import models

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    decription = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    inventory_quantity = models.IntegerField()
    product_images = models.CharField(max_length=255, default = "https://cdn3.f-cdn.com/contestentries/1287460/28855021/5ab5583ddaadd_thumb900.jpg")
   

   # Bonus:How to add image CharField to API Framework 
   # add migrations for img file 
   # def function for image file retrieval 