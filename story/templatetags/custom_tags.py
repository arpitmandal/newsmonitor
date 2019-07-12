from django import template
from django.utils import timezone
from story.models import Story

register = template.Library()

@register.filter
def story(num_post):
    return Story.objects.order_by('-pub_date')