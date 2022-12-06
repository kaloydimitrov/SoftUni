from models_two.web.views import say_hi
from django.urls import path


urlpatterns = (
    path('', say_hi),
)
