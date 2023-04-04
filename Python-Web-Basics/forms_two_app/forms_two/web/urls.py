from django.urls import path, include
from forms_two.web.views import index, home, person, delete_user


urlpatterns = (
   path('', home, name='home'),
   path('register/', index, name='index_name'),
   path('users/', person, name='users'),
   path('users/delete/<int:pk>/', delete_user),

)
