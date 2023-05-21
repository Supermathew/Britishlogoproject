from django import template

register = template.Library()

@register.filter
def custom_range(length):
    return range(0, length, 2)
