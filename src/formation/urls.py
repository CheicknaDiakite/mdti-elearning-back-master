from django.urls import path

from .views import add_formation, add_categorie, del_categorie, get_categorie, set_categorie, add_sous_categorie, \
    get_sous_categorie, del_sous_categorie, set_sous_categorie, get_formation, get_formation_detaille, set_formation, \
    del_formation, add_chapitre, get_chapitre, set_chapitre, del_chapitre, add_discution, get_discution, del_discution, \
    set_discution, add_temoignages, get_temoignages, set_temoignages, del_temoignages, add_cour, set_cour, get_cour, \
    del_cour, add_video_vue, get_video_vue, del_video_vue, get_video, del_video, get_categorie_un, \
    get_sous_categorie_un, get_chapitre_un, set_video, get_all_formation, get_chapitre_all, add_seancetravail, \
    set_seancetravail, del_seancetravail, get_seancetravail, get_detaille_seancetravail, get_all_seancetravail, add_qcm, \
    del_qcm, set_qcm, get_qcm, get_qcm_detail, add_qcm_question, del_qcm_question, set_qcm_question, get_qcm_question, \
    add_qcm_reponse, get_qcm_reponse, set_qcm_reponse, del_qcm_reponse, get_all_qcm_reponse, get_un_qcm_reponse, \
    examen_add, add_video, examen_set, examen_del, examen_get_un, examen_get_all, examen_get, examen_resultat_add, \
    examen_resultat_del, examen_resultat_get, examen_resultat_all, examen_resultat_get_un, get_temoignages_sans_m

urlpatterns = [
    path("add", add_formation, name="add_formation"),
    path("get", get_formation, name="get_formation"),
    path("get-all", get_all_formation, name="get_all_formation"),
    path("get/<str:slug>", get_formation_detaille, name="get_formation_detaille"),
    path("set", set_formation, name="set_formation"),
    path("del", del_formation, name="del_formation"),


    path("categorie/add", add_categorie, name="add_formation"),
    path("categorie/del", del_categorie, name="add_formation"),
    path("categorie/get", get_categorie, name="add_formation"),
    path("categorie/get/<int:id>", get_categorie_un, name="get_categorie_un"),
    path("categorie/set", set_categorie, name="add_formation"),


    path("sous-categorie/add", add_sous_categorie, name="add_formation"),
    path("sous-categorie/set", set_sous_categorie, name="add_formation"),
    path("sous-categorie/get", get_sous_categorie, name="add_formation"),
    path("sous-categorie/get/<int:id>", get_sous_categorie_un, name="add_formation"),
    path("sous-categorie/del", del_sous_categorie, name="add_formation"),


    path("chapitre/add", add_chapitre, name="add_chapitre"),
    path("chapitre/get", get_chapitre, name="add_chapitre"),
    path("chapitre/get-all", get_chapitre_all, name="get_chapitre_all"),
    path("chapitre/get/<int:id>", get_chapitre_un, name="add_chapitre"),
    path("chapitre/set", set_chapitre, name="set_chapitre"),
    path("del_chapitre/set", del_chapitre, name="set_chapitre"),


    path("discution/add", add_discution, name="add_discution"),
    path("discution/get", get_discution, name="get_discution"),
    path("discution/del", del_discution, name="del_discution"),
    path("discution/set", set_discution, name="set_discution"),


    path("temoignages/add", add_temoignages, name="add_temoignages"),
    path("temoignages/get", get_temoignages, name="get_temoignages"),
    path("temoignages/get/sans-m", get_temoignages_sans_m, name="get_temoignages_sans_m"),
    path("temoignages/set", set_temoignages, name="set_temoignages"),
    path("temoignages/del", del_temoignages, name="del_temoignages"),


    path("cour/add", add_cour, name="add_cour"),
    path("cour/set", set_cour, name="set_cour"),
    path("cour/get", get_cour, name="get_cour"),
    path("cour/del", del_cour, name="del_cour"),


    path("video-vue/add", add_video_vue, name="add_video_vue"),
    path("video-vue/get", get_video_vue, name="get_video_vue"),
    path("video-vue/del", del_video_vue, name="del_video_vue"),


    path("video/add/<str:chapitre_id>", add_video, name="add_video"),
    path("video/get", get_video, name="get_video"),
    path("video/del", del_video, name="del_video"),
    path("video/set", set_video, name="set_video"),


    path("seancetravail/add", add_seancetravail, name="add_seancetravail"),
    path("seancetravail/get", get_seancetravail, name="get_seancetravail"),
    path("seancetravail/get-detaille/<int:id>", get_detaille_seancetravail, name="get_detaille_seancetravail"),
    path("seancetravail/get-all", get_all_seancetravail, name="get_all_seancetravail"),
    path("seancetravail/set", set_seancetravail, name="set_seancetravail"),
    path("seancetravail/del", del_seancetravail, name="del_seancetravail"),


    path("qcm/add", add_qcm, name="add_qcm"),
    path("qcm/get", get_qcm, name="get_qcm"),
    path("qcm/get-detail/<int:id>", get_qcm_detail, name="get_qcm_detail"),
    path("qcm/del", del_qcm, name="del_qcm"),
    path("qcm/set", set_qcm, name="set_qcm"),


    path("qcm/question/add", add_qcm_question, name="add_qcm_question"),
    path("qcm/question/del", del_qcm_question, name="del_qcm_question"),
    path("qcm/question/set", set_qcm_question, name="set_qcm_question"),
    path("qcm/question/get", get_qcm_question, name="get_qcm_question"),


    path("qcm/reponse/add", add_qcm_reponse, name="add_qcm_reponse"),
    path("qcm/reponse/get", get_qcm_reponse, name="add_qcm_reponse"),
    path("qcm/reponse/get-all", get_all_qcm_reponse, name="get_all_qcm_reponse"),
    path("qcm/reponse/get/<int:id>", get_un_qcm_reponse, name="get_un_qcm_reponse"),
    path("qcm/reponse/set", set_qcm_reponse, name="add_qcm_reponse"),
    path("qcm/reponse/del", del_qcm_reponse, name="add_qcm_reponse"),


    path("examen/add", examen_add, name="examen_add"),
    path("examen/get/<int:id>", examen_get_un, name="examen_get_un"),
    path("examen/get-all", examen_get_all, name="examen_get_all"),
    path("examen/get", examen_get, name="examen_get"),
    path("examen/set", examen_set, name="examen_set"),
    path("examen/del", examen_del, name="examen_del"),


    path("examen-resultat/add", examen_resultat_add, name="examen_resultat_add"),
    path("examen-resultat/get/<int:id>", examen_resultat_get_un, name="examen_resultat_get_un"),
    path("examen-resultat/get-all", examen_resultat_all, name="examen_resultat_all"),
    path("examen-resultat/get", examen_resultat_get, name="examen_resultat_get"),
    path("examen-resultat/del", examen_resultat_del, name="examen_resultat_del"),

]
