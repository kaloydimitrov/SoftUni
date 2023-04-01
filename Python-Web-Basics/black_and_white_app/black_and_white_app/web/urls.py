from django.urls import path
from black_and_white_app.web.views import index, login

urlpatterns = (
    path('', index, name='index'),
    path('login/', login, name='login')
)
