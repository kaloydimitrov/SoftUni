from django.http import HttpResponse
from django.shortcuts import render
from models_two.web.models import Employees


def home(request):
    return HttpResponse('This is home!')


def employee_details(request):
    context = {
        "employees": Employees.objects.all(),
        "employees_filter": Employees.objects.order_by('first_name', 'last_name'),
        "employees_pk": Employees.objects.get(pk=1),  # Employees.objects.get(department_id=3)
        "employee_department_name": Employees.objects.filter(department__name='Embedded Systems')
    }

    return render(request, 'index.html', context)


def delete_employee(request, pk):
    employee = Employees.objects.get(pk=pk)
    employee.delete()
