from django.urls import path, include
from PizzaGang.web.views import HomeView, RegisterView, SignInView, SignOutView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('identity/', include([
        path('register/', RegisterView.as_view(), name='register'),
        path('sign-in/', SignInView.as_view(), name='sign-in'),
        path('sign-out/', SignOutView.as_view(), name='sign-out')
    ])),
]
