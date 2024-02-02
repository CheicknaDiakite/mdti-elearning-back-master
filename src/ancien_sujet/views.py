import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Type, Niveau, Matiere


# Create your views here.


@csrf_exempt
def add_type_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    if request.method == "POST":
        form = dict()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        if "nom" in form:
            nom = form.get("nom")

            new_type = Type(nom=nom)
            new_type.save()

            response_data["message"] = "success"
            response_data['etat'] = True

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_type_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    types = Type.objects.all()

    all_type = list()

    for t in types:
        all_type.append(
            {
                "id": t.id,
                "nom": t.nom,
            }
        )

    if len(all_type) > 0:
        response_data["etat"] = True
        response_data["message"] = "success"
        response_data["donnee"] = all_type
    else:
        response_data["message"] = "vide"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_type_sujet_un(request, id):
    response_data = {'message': "requette invalide", 'etat': False}

    type = Type.objects.all().filter(id=id).first()

    if type:
        type_data = {
            "id": type.id,
            "nom": type.nom,
        }
        response_data["etat"] = True
        response_data["message"] = "success"
        response_data["donnee"] = type_data

    else:
        response_data["message"] = "type non trouver"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def del_type_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    if request.method == "POST":
        form = dict()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        if "id" in form:
            id = form.get("id")

            type = Type.objects.all().filter(id=id).first()

            if type:
                type.delete()
                response_data["etat"] = True
                response_data["message"] = "success"

            else:
                response_data["message"] = "type non trouver"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


"""
Niveau
"""


@csrf_exempt
def add_niveau_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    if request.method == "POST":
        form = dict()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        if "nom" in form:
            nom = form.get("nom")

            new_niveau = Niveau(nom=nom)
            new_niveau.save()

            response_data["etat"] = True
            response_data["message"] = "success"
            response_data["id"] = new_niveau.id

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_niveau_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    niveau = Niveau.objects.all()

    all_niveau = list()

    for n in niveau:
        all_niveau.append(
            {
                "id": n.id,
                "nom": n.nom,
            }
        )

    if len(all_niveau) > 0:
        response_data["etat"] = True
        response_data["message"] = "success"
        response_data["donnee"] = all_niveau
    else:
        response_data["message"] = "vide"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_un_niveau_sujet(request, id):
    response_data = {'message': "requette invalide", 'etat': False}

    niveau = Niveau.objects.all().filter(id=id).first()

    if niveau:
        data_niveau = {
            "nom": niveau.nom,
            "id": niveau.id,
        }

        response_data["etat"] = True
        response_data["message"] = "success"
        response_data["donnee"] = data_niveau
    else:
        response_data["message"] = "niveau non trouver"


    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def del_niveau_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    if request.method == "POST":
        form = dict()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        if "id" in form:
            id = form.get("id")

            niveau = Niveau.objects.all().filter(id=id).first()

            if niveau:
                niveau.delete()
                response_data["etat"] = True
                response_data["message"] = "success"
            else:
                response_data["message"] = "niveau non trouver"

    return HttpResponse(json.dumps(response_data), content_type="application/json")



"""
Matiere
"""
@csrf_exempt
def add_matiere_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    if request.method == "POST":
        form = dict()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        if "nom" in form:
            nom = form.get("nom")

            new_matiere = Matiere(nom=nom)

            new_matiere.save()
            response_data["etat"] = True
            response_data["id"] = new_matiere.id
            response_data["message"] = "success"


    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def get_matiere_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    matiere = Matiere.objects.all()

    all_matiere = list()
    for m in matiere:
        all_matiere.append(
            {
                "id":m.id,
                "nom":m.nom,
            }
        )

    if len(all_matiere) > 0:
        response_data["etat"] = True
        response_data["message"] = "success"
        response_data["donnee"] = all_matiere
    else:
        response_data["message"]  = "vide"

    return HttpResponse(json.dumps(response_data), content_type="application/json")



@csrf_exempt
def get_matiere_sujet_un(request, id):
    response_data = {'message': "requette invalide", 'etat': False}

    matiere = Matiere.objects.all().filter(id=id).first()

    if matiere:
        response_data["etat"] = True
        response_data["message"] = "success"
        response_data["donnee"] = {
            "id": matiere.id,
            "nom": matiere.nom,
        }
    else:
        response_data["message"]  = "matiere non trouver"

    return HttpResponse(json.dumps(response_data), content_type="application/json")


@csrf_exempt
def del_matiere_sujet(request):
    response_data = {'message': "requette invalide", 'etat': False}

    if request.method == "POST":
        form = dict()
        try:
            form = json.loads(request.body.decode("utf-8"))
        except:
            ...

        if "id" in form:
            id = form.get("id")

            matiere = Matiere.objects.all().filter(id=id).first()

            if matiere:
                matiere.delete()
                response_data["etat"] = True
                response_data["message"] = "success"

            else:
                response_data["message"] = "matiere non trouver"

    return HttpResponse(json.dumps(response_data), content_type="application/json")