# Generated by Django 4.2.8 on 2023-12-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilisateur',
            name='adhesion_public',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='description',
        ),
        migrations.RemoveField(
            model_name='utilisateur',
            name='numero_verifier',
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='type_compte',
            field=models.CharField(choices=[('admin', 'Admin'), ('apprenant', 'Apprenant'), ('instructeur', 'Instructeur')], max_length=300),
        ),
        migrations.DeleteModel(
            name='Emails',
        ),
    ]
