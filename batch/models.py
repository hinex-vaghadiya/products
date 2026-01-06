from django.db import models
from products.models import ProductVariant
# Create your models here.

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    variant = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, related_name="batches")
    qty = models.BigIntegerField()
    mfg_date = models.DateField()
    exp_date = models.DateField()

    def __str__(self):
        return f"{self.variant.name} Batch {self.batch_id}"

