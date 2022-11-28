# Generated by Django 3.2.9 on 2021-11-28 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20211128_1234'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='toolbar',
        ),
        migrations.CreateModel(
            name='ToolbarCell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.PositiveIntegerField(default=0, verbose_name='Ordre')),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toolbar_cell', to='profiles.layoutelement')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toolbar', to='profiles.profile')),
            ],
            options={
                'verbose_name': "Barre d'outils",
                'verbose_name_plural': "Barre d'outils",
                'ordering': ['rank'],
            },
        ),
    ]