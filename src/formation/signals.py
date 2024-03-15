from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Participer


@receiver(pre_save, sender=Participer)
def limiter_enregistrements(sender, instance, **kwargs):
    # Compter le nombre total d'enregistrements avec le même nom de champ
    total_enregistrements = Participer.objects.filter(apprenant=instance.apprenant).count()

    # Si le nombre total d'enregistrements dépasse 2, supprimer le premier enregistrement
    if total_enregistrements > 2:
        Participer.objects.filter(apprenant=instance.apprenant).order_by('id').first().delete()
