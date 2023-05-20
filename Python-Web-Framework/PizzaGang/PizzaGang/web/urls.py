from django.urls import path, include
from PizzaGang.web.views import HomeView, RegisterView, SignInView, SignOutView, ListPizzaView, DetailPizzaView, \
                                add_to_cart, UserInfoAddress, UserInfoBase

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

    path('identity/', include([
        path('register/', RegisterView.as_view(), name='register'),
        path('sign-in/', SignInView.as_view(), name='sign-in'),
        path('sign-out/', SignOutView.as_view(), name='sign-out')
    ])),

    path('menu/', ListPizzaView.as_view(), name='menu'),

    path('pizza/', include([
        path('pizza-details/<int:pk>/', DetailPizzaView.as_view(), name='pizza-details'),
        path('pizza/<int:pizza_pk>/add-to-cart/', add_to_cart, name='cart'),
    ])),


    path('user-info/',include([
        path('details/<int:pk>/', UserInfoAddress.as_view(), name='user-details'),
        path('address')
    ])),
]
