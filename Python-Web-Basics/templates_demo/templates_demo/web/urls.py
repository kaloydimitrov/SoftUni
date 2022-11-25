from django.urls import path
from templates_demo.web.views import index

urlpatterns = (
    path('', index),
)
