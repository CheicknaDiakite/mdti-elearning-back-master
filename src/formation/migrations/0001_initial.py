# Generated by Django 4.2.8 on 2023-12-26 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Chapitre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Cour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prix', models.FloatField()),
                ('date', models.DateField(auto_now_add=True)),
                ('progression', models.FloatField(default=0)),
                ('terminer', models.BooleanField(default=False)),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('miniature', models.ImageField(upload_to='')),
                ('prix', models.FloatField()),
                ('slug', models.SlugField()),
                ('nombre_heur', models.IntegerField()),
                ('description', models.TextField()),
                ('prerequis', models.TextField()),
                ('profile_destine', models.TextField()),
                ('objectif_du_cours', models.TextField()),
                ('publier', models.BooleanField(default=False)),
                ('moderer', models.BooleanField(default=False)),
                ('ajout_terminer', models.BooleanField(default=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('date_de_publication', models.DateField()),
                ('dernier_mise_a_jour', models.DateField(auto_now=True)),
                ('instructeur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('duree', models.IntegerField()),
                ('video', models.FileField(upload_to='')),
                ('chapitre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.chapitre')),
            ],
        ),
        migrations.CreateModel(
            name='VideoVue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('cour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.cour')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.video')),
            ],
        ),
        migrations.CreateModel(
            name='Temoignage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('vue', models.BooleanField(default=False)),
                ('moderer', models.BooleanField(default=False)),
                ('actif', models.BooleanField(default=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.formation')),
            ],
        ),
        migrations.CreateModel(
            name='SousCategorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='')),
                ('slug', models.SlugField()),
                ('categorie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.categorie')),
            ],
        ),
        migrations.AddField(
            model_name='formation',
            name='sous_categorie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.souscategorie'),
        ),
        migrations.CreateModel(
            name='Discution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('lue', models.BooleanField(default=False)),
                ('apprenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('formation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.formation')),
            ],
        ),
        migrations.AddField(
            model_name='cour',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.formation'),
        ),
        migrations.AddField(
            model_name='chapitre',
            name='formation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='formation.formation'),
        ),
    ]