from django import template
from django.utils import timezone
from story.models import Story

register = template.Library()

@register.filter
def story(args):
    return Story.objects.order_by('-pub_date')