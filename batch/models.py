from django.db import models
from products.models import ProductVariant
from django.utils.timezone import now

# Create your models here.

class Batch(models.Model):
    batch_id = models.AutoField(primary_key=True)

    variant = models.ForeignKey(
        ProductVariant,
        on_delete=models.CASCADE,
        related_name="batches"
    )

    batch_code = models.CharField(
        max_length=100,
        unique=True,
        editable=False
    )

    qty = models.BigIntegerField()
    mfg_date = models.DateField()
    exp_date = models.DateField()

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Auto-generate batch_code only on creation
        if not self.batch_code:
            today = now().strftime("%Y%m%d")

            sku = self.variant.sku  # 👈 assumes Variant has sku field

            # Count existing batches for same variant & date
            today_count = Batch.objects.filter(
                variant=self.variant,
                created_at__date=now().date()
            ).count() + 1

            self.batch_code = f"{sku}-{today}-{today_count}"

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.batch_code}"


