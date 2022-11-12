from first_app.tasks.views import index
from django.urls import path

urlpatterns = (
    path('', index)
)
