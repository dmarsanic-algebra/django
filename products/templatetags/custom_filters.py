from django import template
import math


register = template.Library()


@register.filter
def ceil_round(value, decimal_places=2):
    try:
        factor = 10**decimal_places
        return math.ceil(value * factor) / factor
    except (ValueError, TypeError):
        return value
