import json

from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from root.outil import base64_to_image
from .models import Utilisateur


# Create your views here.



# Pour la connexion [POST]
@csrf_exempt
def api_user_login(request):
    response_data = {'message': "requette invalide", 'etat': False}


    if request.method == "POST":
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            form = []
        if "username" in form and "password" in form:
            username = form.get("username")
            password = form.get("password")

            user = authenticate(request, username=username, password=password)
            if user is not None:
                response_data["etat"] = True
                response_data["id"] = user.id
                response_data["message"] = "success"

            else:
                user = Utilisateur.objects.all().filter(username=username).first()
                if user is not None:
                    response_data["message"] = "mot de passe incorrest"
                else:
                    response_data["message"] = "utilisateur non trouvé"


    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def api_user_register(request):
    message = "requette invalide"
    id = ""
    etat = False

    if request.method == "POST":
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            form = []

        # form = json.loads(request.body.decode("utf-8"))
        if ("username" in form
                and "password" in form
                and "first_name" in form
                and "last_name" in form
                and "email" in form
                and "numero"
                and "type_compte" in form):
            username = form.get("username")
            password = form.get("password")
            first_name = form.get("first_name")
            last_name = form.get("last_name")
            email = form.get("email")
            numero = form.get("numero")
            type_compte = form.get("type_compte")

            tmp_user = Utilisateur.objects.all().filter(username=username).first()
            if tmp_user:
                message = "ce non d'utilisateur est déjà utiliser"
            else:
                tmp_user = Utilisateur.objects.all().filter(numero=numero).first()

                if tmp_user:
                    message = "ce numero est déjà utiliser"
                else:
                    tmp_user = Utilisateur.objects.all().filter(email=email).first()

                    if tmp_user:
                        message = "cet email est déjà utiliser"
                    else:
                        Utilisateur.objects.create_user(
                            first_name=first_name,
                            last_name=last_name,
                            username=username,
                            email=email,
                            password=password,
                            type_compte=type_compte,
                            numero=numero)

                        new_utilisateur = authenticate(request, username=username, password=password)
                        etat = True
                        id = new_utilisateur.id
                        message = "success"

                        # TODO send mail ici (mail de bienvenu)


    response_data = {'message': message, 'etat': etat, "id": id}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def api_user_get_profil(request,id):
    message = "requette invalide"
    donnee = dict()
    etat = False


    user_form_data_base = Utilisateur.objects.all().filter(id=id).first()

    if user_form_data_base:
        donnee["first_name"] = user_form_data_base.first_name
        donnee["last_name"] = user_form_data_base.last_name
        donnee["username"] = user_form_data_base.username
        donnee["sexe"] = user_form_data_base.sexe
        donnee["quartier"] = user_form_data_base.quartier
        donnee["travail"] = user_form_data_base.travail
        donnee["date_naissance"] = str(user_form_data_base.date_naissance)
        donnee["mail_verifier"] = user_form_data_base.mail_verifier


        if user_form_data_base.avatar:
            donnee["avatar"] = user_form_data_base.avatar.url
        else:
            donnee["avatar"] = None

        if user_form_data_base.attestation:
            donnee["attestation"] = user_form_data_base.attestation.url
        else:
            donnee["attestation"] = None


        if user_form_data_base.cv:
            donnee["cv"] = user_form_data_base.cv.url
        else:
            donnee["cv"] = None

        donnee["type_compte"] = user_form_data_base.type_compte
        donnee["numero"] = user_form_data_base.numero

        donnee["email"] = user_form_data_base.email

        etat = True
        message = "success"
    else:
        message = "utilisateur non trouvé"

    response_data = {'message': message, 'etat': etat, "donnee": donnee}
    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def api_user_set_profil(request):
    context = {"message":"requette invalide", "etat": False}

    if request.method == "POST":
        form = list()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        # print(form)
        if "utilisateur_id" in form:

            id = form.get("utilisateur_id")

            user_from_data_base = Utilisateur.objects.all().filter(id=id).first()

            modifier = False
            if user_from_data_base:
                if "first_name" in form:
                    first_name = form.get("first_name")
                    user_from_data_base.first_name = first_name
                    modifier = True

                    # user_from_data_base.save()

                if "last_name" in form:
                    last_name = form.get("last_name")
                    user_from_data_base.last_name = last_name
                    modifier = True

                if "quartier" in form:
                    quartier = form.get("quartier")
                    user_from_data_base.quartier = quartier
                    modifier = True

                if "sexe" in form:
                    sexe = form.get("sexe")
                    user_from_data_base.sexe = sexe
                    modifier = True

                if "date_naissance" in form:
                    date_naissance = form.get("date_naissance")
                    user_from_data_base.date_naissance = date_naissance
                    modifier = True

                if "mail_verifier" in form:
                    user_from_data_base.mail_verifier = True
                    modifier = True

                if "travail" in form:
                    travail = form.get("travail")
                    user_from_data_base.travail = travail
                    modifier = True


                if "avatar" in form:

                    avatar_64 = form.get("avatar")

                    avatar = base64_to_image(avatar_64)

                    user_from_data_base.avatar = avatar
                    modifier = True




                if "cv" in form:

                    cv_64 = form.get("cv")

                    cv = base64_to_image(cv_64)

                    user_from_data_base.cv = cv
                    modifier = True


                if "attestation" in form:

                    attestation_64 = form.get("cv")

                    attestation = base64_to_image(attestation_64)

                    user_from_data_base.attestation = attestation
                    modifier = True





                if "numero" in form:
                    numero = form.get("numero")

                    if user_from_data_base.numero != numero:
                        tmp_user = Utilisateur.objects.all().filter(numero=numero).first()
                        tmp_user1 = Utilisateur.objects.all().filter(username=numero).first()
                        if tmp_user or tmp_user1:
                            context["etat"] = False
                            context["message"] = "ce numéro est déjà utilisé"
                        else:
                            user_from_data_base.numero = numero
                            modifier = True
                    else:
                        context["message"] = "ce numéro est déjà utilisé"

                if "email" in form:
                    email = form.get("email")

                    if user_from_data_base.email != email:
                        tmp_user = Utilisateur.objects.all().filter(email=email).first()
                        tmp_user1 = Utilisateur.objects.all().filter(username=email).first()

                        if tmp_user or tmp_user1 :
                            context["etat"] = False
                            context["message"] = "cet email est déjà utilisé"
                        else:
                            user_from_data_base.email = email
                            modifier = True
                    else:
                        context["message"] = "cet email est déjà utilisé"

                if "username" in form:
                    username = form.get("username")

                    if user_from_data_base.username != username:
                        tmp_user = Utilisateur.objects.all().filter(username=username).first()
                        tmp_user1 = Utilisateur.objects.all().filter(numero=username).first()

                        utiliser = False

                        if tmp_user or tmp_user1 or utiliser:
                            context["etat"] = False
                            context["message"] = "ce nom d'utilisateur est déjà utilisé"
                            # print(context)

                        else:
                            user_from_data_base.username = username
                            modifier = True
                    else:
                        context["message"] = "ce nom d'utilisateur est déjà utilisé"

                if "new_password" in form and "old_password" in form:
                    new_password = form.get("new_password")
                    old_password = form.get("old_password")
                    username = user_from_data_base.username

                    user = authenticate(request, username=username, password=old_password)
                    if user:
                        user_from_data_base.set_password(new_password)
                        modifier = True

                    else:
                        context["etat"] = False
                        context["message"] = "Mot de passe incorrect"


                if modifier:
                    user_from_data_base.save()
                    context["etat"] = True
                    context["message"] = "success"
                else:
                    ...
                # TODO requette invalide

            else:
                context["etat"] = False
                context["message"] = "utilisateur non trouvé"
    else:
        context["etat"] = False
        context["message"] = "requette invalide"

    return HttpResponse(json.dumps(context), content_type="application/json")


@csrf_exempt
def api_user_get(request):
    context = {"message":"requette invalide", "etat": False}

    if request.method == "POST":
        form = list()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        filter = False
        all_utilisateur = list()
        if "all" in form:
            all_utilisateur = Utilisateur.objects.all()
            filter = True
        elif "type_compte" in form :
            type_compte = form.get("type_compte")
            all_utilisateur = Utilisateur.objects.all().filter(type_compte=type_compte)
            filter = True

        if filter:
            utilisateurs = list()

            for user in all_utilisateur:
                utilisateurs.append(
                    {
                        "avatar": user.avatar.url if user.avatar else None,
                        "type_compte": user.type_compte,
                        "username": user.username,
                        "first_name": user.first_name,
                        "last_name": user.last_name,
                        "email": user.email,
                        "numero": user.numero ,
                        "sexe": user.sexe if user.sexe else None ,
                        "quartier": user.quartier if user.quartier else None ,
                        "travail": user.travail if user.travail else None ,
                        "date_naissance": str(user.date_naissance) if user.date_naissance else None ,
                    }
                )

            if len(utilisateurs) > 0:
                context['etat'] = True
                context['message'] = "success"
                context['donnee'] = utilisateurs
            else:
                context["etat"] = False
                context["message"] = "vide"


    return HttpResponse(json.dumps(context), content_type="application/json")