from rest_framework import serializers
from products.models import Products

class ProductsSerializer(serializers.ModelSerializer):
    product_id=serializers.ReadOnlyField()
    class Meta:
        model=Products
        fields='__all__'