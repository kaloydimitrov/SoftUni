from django.urls import path, include

'''
http://localhost:8000/ - home page 
http://localhost:8000/profile/create/ - profile create page 
http://localhost:8000/catalogue/ - catalogue 
http://localhost:8000/create/ - plant create page 
http://localhost:8000/details/<plant_id>/ - plant details page 
http://localhost:8000/edit/<plant_id>/ - plant edit page 
http://localhost:8000/delete/<plant_id>/ - plant delete page 
http://localhost:8000/profile/details/ - profile details page 
http://localhost:8000/profile/edit/ - profile edit page 
http://localhost:8000/profile/delete/ - profile delete page 
'''

from .views import index, create_profile, profile_details, edit_profile, delete_profile, \
                        catalogue, create_plant, plant_details, edit_plant, delete_plant


urlpatterns = (
    path('', index, name='home'),

    path('profile/', include([
        path('create/', create_profile, name='profile create'),
        path('details/', profile_details, name='profile details'),
        path('edit/', edit_profile, name='profile edit'),
        path('delete/', delete_profile, name='profile delete')
    ])),

    path('catalogue/', catalogue, name='catalogue'),
    path('create/', create_plant, name='create plant'),
    path('details/<int:pk>/', plant_details, name='plant details'),
    path('edit/<int:pk>/', edit_plant, name='plant edit'),
    path('delete/<int:pk>/', delete_plant, name='plant delete'),

)
