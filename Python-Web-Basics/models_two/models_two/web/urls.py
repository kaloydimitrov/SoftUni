from models_two.web.views import home, employee_details, delete_employee
from django.urls import path

urlpatterns = (
    path('', home),
    path('employees/', employee_details),
    path('employees/delete/<int:pk>/', delete_employee)
)
