from django import template
from ..models import Introduction

register = template.Library()


@register.simple_tag
def get_introduction(tag):
    try:
        introduction = Introduction.objects.get(template_tag=tag)
        return introduction
    except Introduction.DoesNotExist:
        return None
