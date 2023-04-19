from django.urls import path, include
from PizzaGang.web.views import HomeView, RegisterView, SignIn, SignOut

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('identity/', include([
        path('register/', RegisterView.as_view(), name='register'),
        path('login/', SignIn.as_view(), name='signin'),
        path('logout/', SignOut.as_view(), name='signout')
    ])),
]
