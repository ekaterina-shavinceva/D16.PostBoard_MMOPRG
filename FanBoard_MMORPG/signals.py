from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Article


@receiver(post_save, sender=Article)
def article_created(instance, **kwargs):
    print('Новое объявление', instance)
