from django.db import models

# Create your models here.


from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


# Les type de compte utilisateur
class Utilisateur(AbstractUser):
    TYPE_COMPTE = [
        ("Admin", "Admin"),
        ("Apprenant", "Apprenant"),
        ("Instructeur", "Instructeur"),
    ]
    #
    GENRE = [
        ("Homme", "Homme"),
        ("Femme", "Femme"),
    ]

    avatar = models.ImageField(null=True, blank=True)

    type_compte = models.CharField(max_length=300, choices=TYPE_COMPTE)
    numero = models.CharField(max_length=200, blank=True, null=True)
    sexe = models.CharField(max_length=30, verbose_name="Genre", blank=True, null=True)
    quartier = models.CharField(max_length=300, verbose_name="Quartier / ville", blank=True, null=True)
    travail = models.CharField(max_length=300, blank=True, null=True)
    date_naissance = models.DateField(auto_now_add=True, blank=True, null=True)
    mail_verifier = models.BooleanField(default=False)

    cv = models.FileField(null=True, blank=True)
    attestation = models.FileField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} ({self.username})"


class PasswordReset(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    time = models.FloatField()
    utiliser = models.BooleanField(default=False)


class Verification_email(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=512)

    valide = models.BooleanField(default=True)
    date = models.DateField(auto_now=True)
