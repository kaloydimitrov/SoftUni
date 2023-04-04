from django.http import HttpResponse
from django.shortcuts import render


def say_hi(request):
    return HttpResponse('Hello!')
