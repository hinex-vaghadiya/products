from rest_framework import routers
from django.urls import path,include
from products.views import ActivenowView,ProductViewSet,ProductVariantViewSet,ProductImageViewSet,VariantImageViewSet,ProductReviewsView,AddReviewView,AdminReviewViewSet

router=routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'variants', ProductVariantViewSet, basename='variants')
router.register(r'product-images', ProductImageViewSet, basename='product-images')
router.register(r'variant-images', VariantImageViewSet, basename='variant-images')
router.register(r'admin-reviews', AdminReviewViewSet, basename='admin-reviews')


urlpatterns=[
    path('',include(router.urls)),
    path('<str:slug>/reviews/', ProductReviewsView.as_view(), name='product-reviews'),
    path('<str:slug>/reviews/add/', AddReviewView.as_view(), name='add-review'),
    path('active',ActivenowView.as_view()),
]
