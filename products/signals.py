from django.core.cache import cache
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete

from .models import Product

@receiver([post_save, post_delete], sender=Product)
def clear_cache_when_product_save(sender, instance, **kwargs):
    cache.delete_pattern('*shop_list*')