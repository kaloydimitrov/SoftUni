from django.urls import path
from templates_demo.web_demo.views import home, index, display_typo, into_type

urlpatterns = (
    path('', home, name='go-to-home'),
    path('home/', home),
    path('random/', index, name='go-to-random'),
    path('type/', into_type, name='go-to-into_type'),
    path('type/<typo>/', display_typo, name='go-to-type')
)
