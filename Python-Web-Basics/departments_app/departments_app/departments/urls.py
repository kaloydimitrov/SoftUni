from django.urls import path
from departments_app.departments.views import home, department, department_details


urlpatterns = (
    path('', home),
    path('home/', home),
    path('department/', department),
    path('department/<int:department_id>/', department_details)
)
