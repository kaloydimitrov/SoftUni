from models_two.web.views import home, employee_details
from django.urls import path

urlpatterns = (
    path('', home),
    path('employees/', employee_details)
)
