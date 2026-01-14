from rest_framework import serializers
from products.models import ProductImage, VariantImage, ProductVariant, Products
from category.serializers import CategorySerializer
from category.models import Categories


# -------------------------
# IMAGE SERIALIZERS (UPLOAD ENABLED)
# -------------------------
class ProductImageSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(
        queryset=Products.objects.all(),
        write_only=True  # Required to associate the image with a product
    )

    class Meta:
        model = ProductImage
        fields = ['id', 'product', 'image', 'is_primary']


class VariantImageSerializer(serializers.ModelSerializer):
    variant = serializers.PrimaryKeyRelatedField(
        queryset=ProductVariant.objects.all(),
        write_only=True  # Required to associate the image with a variant
    )

    class Meta:
        model = VariantImage
        fields = ['id', 'variant', 'image']


# -------------------------
# PRODUCT VARIANT SERIALIZER
# -------------------------
class ProductVariantSerializer(serializers.ModelSerializer):
    images = VariantImageSerializer(many=True, required=False)  # writable now
    discount_percent = serializers.ReadOnlyField()
    product = serializers.PrimaryKeyRelatedField(queryset=Products.objects.all(), write_only=True)

    class Meta:
        model = ProductVariant
        fields = ['id', 'product', 'name', 'sku', 'price', 'compare_at_price', 'stock', 'discount_percent', 'images']

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        variant = ProductVariant.objects.create(**validated_data)
        for img_data in images_data:
            VariantImage.objects.create(variant=variant, **img_data)
        return variant

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data is not None:
            # Optional: replace all images with new ones
            instance.images.all().delete()
            for img_data in images_data:
                VariantImage.objects.create(variant=instance, **img_data)
        return instance


# -------------------------
# PRODUCT SERIALIZER
# -------------------------
class ProductSerializer(serializers.ModelSerializer):
    variants = ProductVariantSerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, required=False)  # writable
    category = CategorySerializer(source='category_id', read_only=True)  # Nested read-only category
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Categories.objects.all(),
        write_only=True
    )

    class Meta:
        model = Products
        fields = [
            'product_id',
            'product_name',
            'description',
            'is_active',
            'category',      # Read-only nested
            'category_id',   # Write-only field for POST/PUT
            'variants',
            'images',
            'created_at',
            'slug'
        ]

    def create(self, validated_data):
        images_data = validated_data.pop('images', [])
        product = Products.objects.create(**validated_data)
        for img_data in images_data:
            ProductImage.objects.create(product=product, **img_data)
        return product

    def update(self, instance, validated_data):
        images_data = validated_data.pop('images', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if images_data is not None:
            # Optional: replace all images with new ones
            instance.images.all().delete()
            for img_data in images_data:
                ProductImage.objects.create(product=instance, **img_data)
        return instance
