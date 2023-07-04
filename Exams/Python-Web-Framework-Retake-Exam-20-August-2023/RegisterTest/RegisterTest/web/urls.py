from django.urls import path
from .views import HomeView, SignInView, SignOutView, SignUpView

urlpatterns = (
    path('', HomeView, name='home'),
    path('sign-in/', SignInView.as_view(), name='sign_in'),
    path('sign-out/', SignOutView.as_view(), name='sign_out'),
    path('sign-up/', SignUpView.as_view(), name='sign_up')
)
