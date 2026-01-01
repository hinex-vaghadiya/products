from django.db import models
from category.models import Categories
# Create your models here.

# class Products(models.Model):
class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=100)
    product_price=models.BigIntegerField()
    description=models.CharField(max_length=1000)
    stock=models.BigIntegerField()
    category_id=models.ForeignKey(Categories,on_delete=models.CASCADE)
    profile_pic=models.CharField(default="")