from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Products
from products.serializers import ProductsSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .authentication import MicroserviceJWTAuthentication
from rest_framework.views import APIView
# Create your views here.

class ProductsViewset(ModelViewSet):
    # permission_classes=[IsAuthenticated]
    queryset=Products.objects.all()
    serializer_class=ProductsSerializer
    authentication_classes = [MicroserviceJWTAuthentication]

    def get_permissions(self):
        # Allow public access for GET requests
        if self.action in ['list', 'retrieve']:
            return [AllowAny()]
        # Require authentication for other methods
        return [IsAuthenticated()]
class ActivenowView(APIView):
    def get(self,request):
        return Response({"message":"Activated"},status=status.HTTP_200_OK)
