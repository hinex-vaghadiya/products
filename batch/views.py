from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from batch.models import Batch
from batch.serializers import BatchSerializer
from rest_framework.permissions import IsAuthenticated
from .authentication import MicroserviceJWTAuthentication
# Create your views here.

class BatchViewset(ModelViewSet):
    permission_classes=[IsAuthenticated]
    authentication_classes = [MicroserviceJWTAuthentication]
    queryset=Batch.objects.all()
    serializer_class=BatchSerializer