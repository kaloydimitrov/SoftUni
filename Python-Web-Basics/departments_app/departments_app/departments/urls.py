from django.urls import path
from departments_app.departments.views import new_view

urlpatterns = (
    path('', new_view)
)
