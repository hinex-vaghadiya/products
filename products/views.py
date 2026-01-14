from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Products,ProductVariant,ProductImage,VariantImage
from products.serializers import ProductSerializer,ProductVariantSerializer,ProductImageSerializer,VariantImageSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from .authentication import MicroserviceJWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser
# Create your views here.

# -------------------------
# PRODUCT IMAGE UPLOAD
# -------------------------
class ProductImageViewSet(ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer # Read-only for everyone, upload requires auth
    parser_classes = [MultiPartParser, FormParser] 


# -------------------------
# VARIANT IMAGE UPLOAD
# -------------------------
class VariantImageViewSet(ModelViewSet):
    queryset = VariantImage.objects.all()
    serializer_class = VariantImageSerializer
    parser_classes = [MultiPartParser, FormParser] 


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.prefetch_related('variants', 'images').all()
    serializer_class = ProductSerializer
    parser_classes = [MultiPartParser, FormParser]
    lookup_field = "slug"
    lookup_url_kwarg = "slug"

class ProductVariantViewSet(ModelViewSet):
    queryset = ProductVariant.objects.prefetch_related('images').all()
    serializer_class = ProductVariantSerializer
    parser_classes = [MultiPartParser, FormParser] 
    


# class ProductsViewset(ModelViewSet):
#     # permission_classes=[IsAuthenticated]
#     queryset=Products.objects.all()
#     serializer_class=ProductsSerializer
#     authentication_classes = [MicroserviceJWTAuthentication]

#     def get_permissions(self):
#         # Allow public access for GET requests
#         if self.action in ['list', 'retrieve']:
#             return [AllowAny()]
#         # Require authentication for other methods
#         return [IsAuthenticated()]
class ActivenowView(APIView):
    def get(self,request):
        return Response({"message":"Activated"},status=status.HTTP_200_OK)
