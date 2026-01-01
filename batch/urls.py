from rest_framework import routers
from django.urls import path,include
from batch.views import BatchViewset

router=routers.DefaultRouter()
router.register(r'batch',BatchViewset)

urlpatterns=[
    path('',include(router.urls))
]