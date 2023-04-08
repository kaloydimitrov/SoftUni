from django.urls import path
from class_based_views_app.web.views import *

urlpatterns = [
    path('', main),
    path('fbv/', FBV, name='fbv'),
    path('cbv/', CBV.as_view(), name='cbv'),
    path('tv/', TV.as_view(), name='tv'),
    path('task-list/', TaskList.as_view(), name='lv'),
    path('task-details/<int:pk>/', TaskDetails.as_view(), name='lv-d'),
    path('task-create/', TaskCreate.as_view(), name='cv'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='uv'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='dv'),
]
