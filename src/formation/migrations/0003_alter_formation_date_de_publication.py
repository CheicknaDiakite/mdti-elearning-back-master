# Generated by Django 4.2.8 on 2023-12-27 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0002_alter_formation_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='date_de_publication',
            field=models.DateField(blank=True, null=True),
        ),
    ]
