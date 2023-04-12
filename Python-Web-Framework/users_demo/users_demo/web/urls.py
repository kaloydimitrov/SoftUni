from django.urls import path
from users_demo.web.views import index, UserRegister, UserLogIn, UserLogOut, UserDetails

urlpatterns = (
    path('', index, name='home'),
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogIn.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('user-info/<int:pk>/', UserDetails.as_view(), name='user-details')
)
