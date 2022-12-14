# Generated by Django 3.2.9 on 2021-11-14 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('nav', '0002_auto_20211114_1919'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchEngine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('template_url', models.CharField(help_text="{root_url} sera remplacé par l'url de l'application. {search_query} sera remplacé par la recherche de l'utilisateur", max_length=255, verbose_name="Modèle d'URL")),
                ('name', models.CharField(max_length=100, verbose_name='Nom')),
                ('parent_app', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='app', to='nav.tabletappconfig')),
            ],
            options={
                'verbose_name': 'Moteur de recherche',
                'verbose_name_plural': 'Moteurs de recherche',
            },
        ),
    ]
