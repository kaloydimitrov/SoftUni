from models_two.web.views import home, employee_details, employee_delete, employee_info
from django.urls import path

urlpatterns = (
    path('', home),
    path('employees/', employee_details),
    path('employees/delete/<int:pk>/', employee_delete),
    path('employees/show/<int:pk>/', employee_info),
)
