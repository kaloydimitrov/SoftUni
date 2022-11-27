import random

from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    context = {

    }

    return render(request, 'home.html', context)


def display_typo(request, typo):
    if typo == '0':
        response = '0 (zero) is a number representing an empty quantity. In place-value notation such as the ' \
                   'Hindu–Arabic numeral system, 0 also serves as a placeholder numerical digit, which works by ' \
                   'multiplying digits to the left of 0 by the radix, usually by 10. As a number, 0 fulfills a ' \
                   'central role in mathematics as the additive identity of the integers, real numbers, ' \
                   'and other algebraic structures. '
    elif typo == '1':
        response = '1 (one, unit, unity) is a number representing a single or the only entity. 1 is also a numerical ' \
                   'digit and represents a single unit of counting or measurement. For example, a line segment of ' \
                   'unit length is a line segment of length 1. In conventions of sign where zero is considered ' \
                   'neither positive nor negative, 1 is the first and smallest positive integer.[1] It is also ' \
                   'sometimes considered the first of the infinite sequence of natural numbers, followed by 2, ' \
                   'although by other definitions 1 is the second natural number, following 0. '
    else:
        response = f'You typed: {typo}'

    return HttpResponse(response)


def index(request):
    context = {
        'random_color': random.choice(['red', 'blue', 'green']),
        'random_number': random.randint(0, 100),

        'random_numbers': [random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)],


        'dictionary': {
            'val1': 1,
            'val2': 2,
            'val3': 3
        },

        'text': "If you're looking for random paragraphs, you've come to the right place. ",

        'colors': ['red', 'blue', 'green'],

        'value': False,

        'float': 1.2536304578,

        'values': [1, 5, 10, 2, 7],
    }

    return render(request, 'index.html', context)
