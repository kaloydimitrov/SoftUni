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
        path('add/', add_album, name='add album page'),
        path('details/<int:id>/', details_album, name='album details page'),
        path('edit/<int:id>/', edit_album, name='edit album page'),
        path('delete/<int:id>/', delete_album, name='delete album page'),
    ])),
    path('profile/', include([
        path('details/', details_profile, name='profile details page'),
        path('delete/', delete_profile, name='delete profile page'),
    ]))
)
