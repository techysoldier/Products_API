from email.mime import image
from rest_framework import serializers 
from .models import Product

class ProductSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product 
        fields = ['id', 'title', 'decription','price', 'inventory_quantity', 'product_images']
        