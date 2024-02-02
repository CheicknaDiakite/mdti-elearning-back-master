from django.db import models


# Create your models here.


class Type(models.Model):
    nom = models.CharField(max_length=255)


class Niveau(models.Model):
    nom = models.CharField(max_length=255)


class Matiere(models.Model):
    nom = models.CharField(max_length=255)

class Pays(models.Model):
    nom = models.CharField(max_length=255)


class Document(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    niveau = models.ForeignKey(Niveau, on_delete=models.CASCADE)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)

    nom = models.CharField(max_length=255)
    annee = models.CharField(max_length=255)

    document = models.FileField()

    prix = models.IntegerField()
    miniature = models.ImageField()
    date = models.DateField(auto_now_add=True)