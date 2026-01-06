from rest_framework import serializers

from category.models import Categories

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category_id', 'category_name']


