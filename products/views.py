from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework.permissions import IsAuthenticated
from .authentication import MicroserviceJWTAuthentication
# Create your views here.

class ProductsViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes = [MicroserviceJWTAuthentication]
    queryset=Products.objects.all()
    serializer_class=ProductsSerializer
    