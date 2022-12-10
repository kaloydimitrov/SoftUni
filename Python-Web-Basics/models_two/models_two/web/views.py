from django.http import HttpResponse
from django.shortcuts import render, redirect
from models_two.web.models import Employees, Departments


def home(request):
    return render(request, 'home_page.html')


def employee_details(request):
    context = {
        "employees": Employees.objects.all(),
        # "employees_filter": Employees.objects.order_by('first_name', 'last_name'),
        # "employees_pk": Employees.objects.get(pk=1),  # Employees.objects.get(department_id=1)
        # "employee_department_name": Employees.objects.filter(department__name='Embedded Systems')
    }

    return render(request, 'main_employee_page.html', context)


def employee_delete(request, pk):
    employee = Employees.objects.get(pk=pk)
    employee.delete()

    context = {
        "employee": employee
    }

    return render(request, 'delete_employee_message.html', context)


def employee_info(request, pk):
    context = {
        "employee": Employees.objects.get(pk=pk)
    }

    return render(request, 'show_employee_info.html', context)
