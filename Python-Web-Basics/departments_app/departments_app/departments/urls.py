from django.urls import path
from departments_app.departments.views import home, department, department_details, department_details_html, \
    department_details_template, redirect_to_home, raising_error


urlpatterns = (
    path('', home),
    path('home/', home),
    path('department/', department),
    path('department/<int:department_id>/', department_details_template),
    path('go-to-home/', redirect_to_home, name='go to home'),
    path('not-found/', raising_error),
)
