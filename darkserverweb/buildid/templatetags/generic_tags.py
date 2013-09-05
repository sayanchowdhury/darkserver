from django import template

register = template.Library()

@register.filter
def dictionary(value, arg):
    if type(value) != dict:
        return ''

    try:
        ret = value[arg]
        return ret
    except KeyError:
        return ''
