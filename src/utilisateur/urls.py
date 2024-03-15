from django.urls import path

from .views import api_user_login, api_user_register, api_user_get_profil, api_user_set_profil, api_user_get

urlpatterns = [
    path("connexion", api_user_login, name="connexion"),
    path("inscription", api_user_register, name="api_user_register"),
    path("profile/get/<int:id>", api_user_get_profil, name="api_user_get_profil"),
    path("profile/set", api_user_set_profil, name="api_user_set_profil"),
    path("get", api_user_get, name="api_user_get"),
]
