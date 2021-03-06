'''
doc: `https://docs.djangoproject.com/en/3.1/howto/custom-template-tags/`
'''
from django import template
from django.utils.safestring import mark_safe
from events.models import UserLikeEvent

register = template.Library()


@register.simple_tag
def is_favorite(user, event):
    try:
        is_favorite = UserLikeEvent.objects.get(user=user, event=event)
        if is_favorite:
            return mark_safe('favorite')
        else:
            return mark_safe('favorite_border')    
    except:
        return mark_safe('favorite_border')