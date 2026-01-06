from rest_framework import routers
from django.urls import path,include
from products.views import ProductsViewset,ActivenowView

router=routers.DefaultRouter()
router.register(r'products',ProductsViewset)
router.register(r'active',ActivenowView)

urlpatterns=[
    path('',include(router.urls))
]
