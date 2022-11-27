from django.urls import path
from models_demo.web_demo.views import say_hi


urlpatterns = (
    path('', say_hi),
)
