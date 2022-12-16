import random
from PyDictionary import PyDictionary

dc = PyDictionary()

from django.shortcuts import render


def home(request):
    context = {

    }

    return render(request, 'home.html', context)


def into_type(request):
    return render(request, 'into_type.html')


def display_typo(request, typo):
    mn = dc.meaning(typo)

    context = {
        'typo': typo,
        'result': mn,
        'result_nouns': mn['Noun'],
        'result_verbs': mn['Verb'],
    }

    return render(request, 'type.html', context)


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
