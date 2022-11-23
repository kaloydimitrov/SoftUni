from django.urls import path
from departments_app.departments.views import home, department


urlpatterns = (
    path('', home),
    path('home/', home),
    path('departmnet/', department)
)
