# Generated by Django 4.2.8 on 2024-01-31 10:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ancien_sujet', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='document',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='document',
            field=models.FileField(default='df', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='document',
            name='pays',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ancien_sujet.pays'),
            preserve_default=False,
        ),
    ]