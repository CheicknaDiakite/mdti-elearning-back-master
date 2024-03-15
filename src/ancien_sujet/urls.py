from django.urls import path

from .views import add_type_sujet, get_type_sujet, get_type_sujet_un, del_type_sujet, add_niveau_sujet, \
    get_niveau_sujet, get_un_niveau_sujet, del_niveau_sujet, add_matiere_sujet, get_matiere_sujet, get_matiere_sujet_un, \
    del_matiere_sujet

urlpatterns = [
    path("type/add",add_type_sujet, name="add_type_sujet"),
    path("type/get",get_type_sujet, name="get_type_sujet"),
    path("type/get/<int:id>",get_type_sujet_un, name="get_type_sujet_un"),
    path("type/del",del_type_sujet, name="del_type_sujet"),


    path("niveau/add",add_niveau_sujet, name="add_niveau_sujet"),
    path("niveau/get",get_niveau_sujet, name="get_niveau_sujet"),
    path("niveau/get/<int:id>",get_un_niveau_sujet, name="get_un_niveau_sujet"),
    path("niveau/del",del_niveau_sujet, name="del_niveau_sujet"),


    path("matiere/add",add_matiere_sujet, name="add_matiere_sujet"),
    path("matiere/get",get_matiere_sujet, name="get_matiere_sujet"),
    path("matiere/get/<int:id>",get_matiere_sujet_un, name="get_matiere_sujet_un"),
    path("matiere/del",del_matiere_sujet, name="del_matiere_sujet"),
]