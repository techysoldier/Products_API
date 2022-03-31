from django.shortcuts import get_object_or_404
from telnetlib import STATUS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product
from products import serializers


@api_view(['GET', 'POST'])
def products_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT'])
def product_detail(request, pk):
    product = get_object_or_404(Product, pk =pk)
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
         


    # car = get_object_or_404(Product, pk=pk)

    # if request.method == 'GET':
    #    serializer = ProductSerializer(car);
    #    return Response(serializer.data)
   
        

    
# @api_view(['GET', 'PUT', 'DELETE'])
# def cars_detail(request, pk):
#     car = get_object_or_404(Car, pk=pk)

#     if request.method == 'GET':
#        serializer = CarSerializer(car);
#        return Response(serializer.data)

#     elif request.method == 'PUT':
#        car = get_object_or_404(Car, pk=pk)
#        serializer = CarSerializer(car, data=request.data )
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data)





#     elif request.method == 'PUT':
#        product = get_object_or_404(Product, pk=pk)
#        serializer = ProductSerializer(product, data=request.data )
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data)

#     elif request.method == "DELETE":
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)