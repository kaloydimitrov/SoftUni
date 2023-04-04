from django.urls import path
from class_based_views_app.web.views import *

urlpatterns = (
    path('', main),
    path('fbv/', FBV, name='fbv'),
    path('cbv/', CBV.as_view(), name='cbv'),
    path('tv/', TV.as_view(), name='TV')
)
