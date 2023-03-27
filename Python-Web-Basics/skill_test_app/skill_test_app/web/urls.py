from skill_test_app.web.views import index, create_user, delete_user, user_info
from django.urls import path

urlpatterns = (
    path('', index, name='index'),
    path('login/', create_user, name='create-user'),
    path('delete/<pk>', delete_user),
    path('info/<pk>', user_info)
)
