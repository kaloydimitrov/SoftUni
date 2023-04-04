from django.urls import path
from forms_demo.web.views import home, forms


urlpatterns = (
    path('', home, name='home'),
    path('forms/', forms, name='forms')
)
