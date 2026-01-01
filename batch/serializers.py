from rest_framework import serializers
from batch.models import Batch
class BatchSerializer(serializers.ModelSerializer):
    batch_id=serializers.ReadOnlyField()
    class Meta:
        model=Batch
        fields='__all__'
