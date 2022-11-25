from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound


def home(request):
    return HttpResponse(f'{request.method}: This is home')


def department(request):
    return HttpResponse(f'{request.method}: This is department (default)')


def department_details(request, department_id):
    return HttpResponse(f'{request.method}: This is department {department_id}')


def department_details_html(request, department_id):
    department_name = ''

    if department_id == 1:
        department_name = 'Developers'
    elif department_id == 2:
        department_name = 'Trainers'

    html = '<html><body><h1>' \
           f'Department name: {department_name}, Department ID {department_id}' \
           '</html></body></h1>'

    return HttpResponse(html)


def department_details_template(request, department_id):
    context = {
        'department_name': 'random name',
        'department_id': department_id
    }

    return render(request=request, template_name='departments/main.html', context=context)


def redirect_to_home(request):
    return redirect(to='http://127.0.0.1:8000/')


def raising_error(request):
    return HttpResponseNotFound('This is not found')
