from django.urls import path
from forms_demo.web.views import home, index

urlpatterns = (
    path('', home, name='home'),
    path('forms/', index)
)
