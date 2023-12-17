from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from cuentas.views import login_request, register_request, editar_request, editar_avatar_request, mi_perfil

urlpatterns = [
    path('login/', login_request, name="Login"),
    path('logout/', LogoutView.as_view(template_name="cuentas/logout.html"), name="Logout"),
    path('registro/', register_request, name="Registro"),
    path('editar_perfil/', editar_request, name="EditarPerfil"),
    path('avatar/', editar_avatar_request, name="Avatar"),
    path('perfil/', mi_perfil, name="Perfil"),
]