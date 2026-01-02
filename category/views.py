from django.shortcuts import render
from rest_framework.response import Response
from category.serializers import CategoriesSerializer
from rest_framework.viewsets import ModelViewSet
from category.models import Categories
from rest_framework.permissions import IsAuthenticated, AllowAny
from .authentication import MicroserviceJWTAuthentication


class CategoriesViewset(ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    authentication_classes = [MicroserviceJWTAuthentication]

    def get_permissions(self):
        # Allow public access for GET requests
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        # Require authentication for other methods
        return [IsAuthenticated()]
