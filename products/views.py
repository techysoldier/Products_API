from telnetlib import STATUS
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer
from .models import Product


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

#     elif request.method == "DELETE":
#         car.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)