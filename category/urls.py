from django.urls import path

from rest_framework import routers
from category.views import CategoriesViewset

router=routers.DefaultRouter()
router.register(r'category',CategoriesViewset)
from django.urls import path,include

urlpatterns = [
    path('',include(router.urls)),
]