# Generated by Django 4.2.8 on 2024-01-09 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0007_examen_qcm_question_reponse_resultatexamen_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='seancetravail',
            name='confirmer_par_apprenant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='seancetravail',
            name='confirmer_par_instructeur',
            field=models.BooleanField(default=False),
        ),
    ]
