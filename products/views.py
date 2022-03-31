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

@api_view(['GET'])
def product_detail(request, pk):
    try:
        product =Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    # car = get_object_or_404(Product, pk=pk)

    # if request.method == 'GET':
    #    serializer = ProductSerializer(car);
    #    return Response(serializer.data)
   
        




#     elif request.method == 'PUT':
#        product = get_object_or_404(Product, pk=pk)
#        serializer = ProductSerializer(product, data=request.data )
#        serializer.is_valid(raise_exception=True)
#        serializer.save()
#        return Response(serializer.data)

#     elif request.method == "DELETE":
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)