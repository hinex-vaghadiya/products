from django.urls import path

from rest_framework import routers
from category.views import CategoryViewSet

router=routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
from django.urls import path,include

urlpatterns = [
    path('',include(router.urls)),
]