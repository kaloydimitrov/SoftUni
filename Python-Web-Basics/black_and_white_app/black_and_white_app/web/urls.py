from django.urls import path
from black_and_white_app.web.views import say_hi, login

urlpatterns = (
    path('', say_hi, name='index'),
    path('login/', login, name='login')
)
