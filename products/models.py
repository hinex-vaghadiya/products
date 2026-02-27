from django.db import models
from category.models import Categories
import uuid
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
# Create your models here.

# class Products(models.Model):
class Products(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True) 
    description = models.CharField(max_length=1000)
    category_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="products")
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.product_name)
            slug = base_slug
            count = 1
            while Products.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{count}"
                count += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name



class ProductVariant(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="variants")
    name = models.CharField(max_length=100)  # e.g., "Pack of 6", "500 ml"
    sku = models.CharField(max_length=100, unique=True, blank=True)
    price = models.BigIntegerField()
    compare_at_price = models.BigIntegerField(null=True, blank=True)
    stock = models.BigIntegerField()
    is_active = models.BooleanField(default=True)

    def discount_percent(self):
        if self.compare_at_price:
            return int(((self.compare_at_price - self.price) / self.compare_at_price) * 100)
        return 0

    def save(self, *args, **kwargs):
        if self.pk:
            original = ProductVariant.objects.get(pk=self.pk)
            if original.sku != self.sku:
                raise ValueError("SKU cannot be changed once created")

        if not self.sku:
            product_part = slugify(self.product.product_name)[:10].upper()
            variant_part = slugify(self.name)[:10].upper()
            unique_part = uuid.uuid4().hex[:6].upper()
            self.sku = f"{product_part}-{variant_part}-{unique_part}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.product.product_name} - {self.name}"

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['product', 'name'], name='unique_product_variant')
        ]


class ProductImage(models.Model):
    product = models.ForeignKey(Products, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField('image')
    is_primary = models.BooleanField(default=False)

class VariantImage(models.Model):
    variant = models.ForeignKey(ProductVariant, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField('image')

class Review(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="reviews")
    user_id = models.IntegerField()
    rating = models.IntegerField()
    review_text = models.TextField()
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_id} on {self.product.product_name}"
