from django.urls import path
from departments_app.departments.views import home, department, department_details, department_details_html


urlpatterns = (
    path('', home),
    path('home/', home),
    path('department/', department),
    path('department/<int:department_id>/', department_details_html)
)
