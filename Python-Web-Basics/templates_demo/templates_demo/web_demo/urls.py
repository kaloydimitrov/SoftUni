from django.urls import path
from templates_demo.web_demo.views import home, index, display_typo

urlpatterns = (
    path('', home),
    path('home/', home),
    path('random/', index),
    path('type/<typo>/', display_typo)
)
