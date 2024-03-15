# Generated by Django 4.2.8 on 2024-01-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0002_remove_utilisateur_adhesion_public_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='attestation',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='utilisateur',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='utilisateur',
            name='type_compte',
            field=models.CharField(choices=[('Admin', 'Admin'), ('Apprenant', 'Apprenant'), ('Instructeur', 'Instructeur')], max_length=300),
        ),
    ]