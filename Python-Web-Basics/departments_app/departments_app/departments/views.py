from django.shortcuts import render


def say_hi(request, *args, **kwargs):
    print(args)
    print(kwargs)
