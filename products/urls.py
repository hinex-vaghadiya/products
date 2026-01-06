from rest_framework import routers
from django.urls import path,include
from products.views import ProductsViewset,ActivenowView

router=routers.DefaultRouter()
router.register(r'products',ProductsViewset)


urlpatterns=[
    path('',include(router.urls)),
    path('active',ActivenowView.as_view()),
]
