from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from products.models import Products,ProductVariant,ProductImage,VariantImage,Review
from products.serializers import ProductSerializer,ProductVariantSerializer,ProductImageSerializer,VariantImageSerializer,ReviewSerializer
import requests
import os
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

class ProductReviewsView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, slug):
        product = Products.objects.filter(slug=slug).first()
        if not product:
            return Response({"error": "Product not found"}, status=404)
        reviews = Review.objects.filter(product=product, is_approved=True)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

class AddReviewView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, slug):
        product = Products.objects.filter(slug=slug).first()
        if not product:
            return Response({"error": "Product not found"}, status=404)
        
        user_id = request.data.get('user_id')
        rating = request.data.get('rating')
        review_text = request.data.get('review_text')

        CART_URL = os.environ.get('CART_URL', 'http://127.0.0.1:8001/api/')
        try:
            resp = requests.get(f"{CART_URL}verify-purchase/{user_id}/{product.product_id}/")
            if resp.status_code == 200 and resp.json().get('has_purchased'):
                pass
            else:
                return Response({"error": "You must purchase and receive this product before reviewing."}, status=400)
        except Exception as e:
            pass # allow in dev if carts is unreachable

        review = Review.objects.create(
            product=product,
            user_id=user_id,
            rating=rating,
            review_text=review_text
        )
        serializer = ReviewSerializer(review)
        return Response(serializer.data, status=201)

class AdminReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]
