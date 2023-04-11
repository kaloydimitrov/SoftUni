from django.urls import path
from users_demo.web.views import index, UserRegister, UserLogin, UserDetails

urlpatterns = (
    path('', index, name='home'),
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('user-info/<int:pk>/', UserDetails.as_view(), name='user-details')
)
