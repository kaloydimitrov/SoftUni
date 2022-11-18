from django.urls import path
from departments_app.departments.views import say_hi

urlpatterns = (
    path('', say_hi)
)
