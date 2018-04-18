from django.db.models.signals import post_save
from django.dispatch import receiver

from warehouse.models import *

@receiver(post_save, sender=WorkOrder)
def work_order_versa_creation(sender, instance, created, **kwargs):
    if instance and created:
        current_inst = instance.quantity
        for i in range(current_inst):
