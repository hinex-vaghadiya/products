from rest_framework import routers
from django.urls import path,include
from batch.views import BatchViewSet

router=routers.DefaultRouter()
router.register(r'batches', BatchViewSet)

urlpatterns=[
    path('',include(router.urls))
]