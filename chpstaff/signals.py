from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Account


@receiver(post_save, sender=Account)
def create_account(sender, instance, created, **kwargs):
    if created:
        Account.objects.create(chpstaff=instance)


@receiver(post_save, sender=Account)
def save_account(sender, instance, **kwargs):
    instance.account.save()