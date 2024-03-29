from django.urls import path
from users_demo.web.views import index, add_to_cart, UserRegister, UserLogIn, UserLogOut, UserDetails, BuyPizza, ListPizza

urlpatterns = (
    path('', index, name='home'),
    path('register/', UserRegister.as_view(), name='register'),
    path('login/', UserLogIn.as_view(), name='login'),
    path('logout/', UserLogOut.as_view(), name='logout'),
    path('user-info/<int:pk>/', UserDetails.as_view(), name='user-details'),
    path('menu/', ListPizza.as_view(), name='menu'),
    path('pizza-info/<int:pk>/', BuyPizza.as_view(), name='pizza-details'),
    path('add-to-cart/<int:pizza_id>/<str:size>/', add_to_cart, name='add-to-cart'),
)
