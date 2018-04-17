from django import template
from django.contrib.auth.models import Group

register = template.Library()

@register.filter(name='in_group')
def in_group(user, group):
    try:
        group = Group.objects.get(name=group)
    except Group.DoesNotExist:
        return False
    return group in user.groups.all()
