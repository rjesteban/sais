from django import template

register = template.Library()


@register.filter(name='subt')
def subt(value, arg):
    return value - arg
