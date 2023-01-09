from django.urls import path, include
from .views import *


'''
http://localhost:8000/ - home page
http://localhost:8000/album/add/ - add album page
http://localhost:8000/album/details/<id>/ - album details page
http://localhost:8000/album/edit/<id>/ - edit album page
http://localhost:8000/album/delete/<id>/ - delete album page
http://localhost:8000/profile/details/ - profile details page
http://localhost:8000/profile/delete/ - delete profile page
'''

urlpatterns = (
    path('', index, name='home'),
    path('album/', include([
        path('add/', add_album, name='add album'),
        path('details/<int:pk>/', details_album, name='album details'),
        path('edit/<int:pk>/', edit_album, name='edit album'),
        path('delete/<int:pk>/', delete_album, name='delete album'),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='profile details'),
        path('delete/', delete_profile, name='delete profile'),
        path('edit/', edit_profile, name='edit profile')
    ]))
)
