from django.urls import path, include
from CRUD_fb_views_cb_views.web.views import HomeView, TaskUpdate


urlpatterns = (
    path('', HomeView, name='home'),
    path('task-update<int:pk>', TaskUpdate, name='task-update')
)
