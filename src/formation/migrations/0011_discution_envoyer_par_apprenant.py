# Generated by Django 4.2.8 on 2024-01-12 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0010_rename_lien_de_la_reusion_seancetravail_lien_de_la_reunion'),
    ]

    operations = [
        migrations.AddField(
            model_name='discution',
            name='envoyer_par_apprenant',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
