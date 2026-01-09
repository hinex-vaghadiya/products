# batch/signals.py
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.db.models import Sum
from .models import Batch
from products.models import ProductVariant


def update_variant_stock(variant):
    total_qty = (
        Batch.objects
        .filter(variant=variant, is_active=True)
        .aggregate(total=Sum('qty'))['total']
        or 0
    )

    ProductVariant.objects.filter(id=variant.id).update(stock=total_qty)


@receiver(post_save, sender=Batch)
def batch_saved(sender, instance, **kwargs):
    update_variant_stock(instance.variant)


@receiver(post_delete, sender=Batch)
def batch_deleted(sender, instance, **kwargs):
    update_variant_stock(instance.variant)
