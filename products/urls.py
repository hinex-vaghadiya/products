from rest_framework import routers
from django.urls import path,include
from products.views import ActivenowView,ProductViewSet,ProductVariantViewSet,ProductImageViewSet,VariantImageViewSet

router=routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'variants', ProductVariantViewSet, basename='variants')
router.register(r'product-images', ProductImageViewSet, basename='product-images')
router.register(r'variant-images', VariantImageViewSet, basename='variant-images')


urlpatterns=[
    path('',include(router.urls)),
    path('active',ActivenowView.as_view()),
]
