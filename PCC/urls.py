from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("usuario/", include('usuario.urls')),
    path("accounts/", include(urls)),
    path("sistema/", include('sistema.urls')),

]
