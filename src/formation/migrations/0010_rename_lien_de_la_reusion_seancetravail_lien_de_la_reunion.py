# Generated by Django 4.2.8 on 2024-01-09 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0009_seancetravail_lien_de_la_reusion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seancetravail',
            old_name='lien_de_la_reusion',
            new_name='lien_de_la_reunion',
        ),
    ]