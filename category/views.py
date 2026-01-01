from django.shortcuts import render
from rest_framework.response import Response
from category.serializers import CategoriesSerializer
from rest_framework.viewsets import ModelViewSet
from category.models import Categories
from rest_framework.permissions import IsAuthenticated
from .authentication import MicroserviceJWTAuthentication
# Create your views here.


class CategoriesViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes = [MicroserviceJWTAuthentication]
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer