from django import template

register = template.Library()


@register.filter(name='odd')
def list_odd_numbers(numbers):
    return [n for n in numbers if n % 2 == 1]
