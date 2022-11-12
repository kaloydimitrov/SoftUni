# Create your views here.
from django.urls import path
from first_app.tasks.views import show_views, show_all_tasks

urlpatterns = (
    path('', show_views),
    path('all/', show_all_tasks),
)
