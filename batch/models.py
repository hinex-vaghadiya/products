from django.db import models
from products.models import Products
# Create your models here.

class Batch(models.Model):
    batch_id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    qty=models.BigIntegerField()
    Mfg_date=models.DateField()
    Exp_date=models.DateField()
