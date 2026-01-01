from rest_framework import serializers

from category.models import Categories

class CategoriesSerializer(serializers.ModelSerializer):
    user_id=serializers.ReadOnlyField()
    class Meta:
        model=Categories
        fields='__all__'

