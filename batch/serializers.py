from rest_framework import serializers
from batch.models import Batch

class BatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Batch
        fields = ['batch_id', 'variant', 'qty', 'mfg_date', 'exp_date','is_active','batch_code']