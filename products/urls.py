from rest_framework import routers
from django.urls import path,include
from products.views import ProductsViewset

router=routers.DefaultRouter()
router.register(r'products',ProductsViewset)

urlpatterns=[
    path('',include(router.urls))
]