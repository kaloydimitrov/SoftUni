from django.urls import path, include

from Stylehive.web.views import IndexView

urlpatterns = (
    path('', IndexView.as_view(), name='home'),
)
