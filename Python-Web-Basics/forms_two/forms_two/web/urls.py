from django.urls import path
from forms_two.web.views import index, home, person


urlpatterns = (
   path('', home, name='home'),
   path('register/', index, name='index_name'),
   path('users/', person, name='users')
)
