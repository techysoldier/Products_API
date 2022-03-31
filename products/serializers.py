from pyexpat import model
from rest_framework import serializers 
from .models import Product

class CarSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = Product 
        fields = ['id', 'title', 'decription','price', 'inventory_quantity']
        