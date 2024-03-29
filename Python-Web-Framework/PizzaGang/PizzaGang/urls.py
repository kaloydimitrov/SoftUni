from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('PizzaGang.web.urls')),
    path('', include('PizzaGang.cart.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'PizzaGang.web.views.handler404'
