from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from .serializers import ProductSerializer
from .models import Product

# Create your views here.
class apiOverview(APIView):
    def get(self, request):
        api_urls = {
            'List': '/product/list/',
            'Detail view': '/product/detail/<init:id>',
            'Create': '/product/create/',
            'Update': '/product/update/<int:id>',
            'Delete': '/product/delete/<int:id>'
        }
        return Response(api_urls)
    
class ShowAll(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    
class ViewProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

class CreateProduct(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)
    
class UpdateProduct(APIView):
    def put(self, request, pk):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
        
        return Response(serializer.data)
    
class DeleteProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(id=pk)
        product.delete()
        
        return Response('Deleted Successfully')