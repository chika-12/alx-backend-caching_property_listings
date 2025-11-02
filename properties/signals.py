from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.core.cache import cache
from .models import Property

@receiver(post_save, sender=Property)
def clear_cache_on_save(sender, instance, **kwarg):
  cache.delete("property_list")
  print("Cache cleared after proprty save")

@receiver(post_delete, sender=Property)
def clear_cache_on_delete(sender, instance, **kwarg):
  cache.delete("property_list")