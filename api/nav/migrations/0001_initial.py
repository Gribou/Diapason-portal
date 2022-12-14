# Generated by Django 3.2.5 on 2021-10-27 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nom')),
                ('label', models.CharField(max_length=100, verbose_name="Nom d'affichage")),
                ('rank', models.PositiveIntegerField(default=0, verbose_name='Ordre')),
                ('icon', models.FileField(blank=True, help_text="Image SVG de couleur blanche de préférence (issue par ex de : <a href='https://materialdesignicons.com/'>https://materialdesignicons.com/</a> )", max_length=250, upload_to='categories', verbose_name='Icône')),
            ],
            options={
                'verbose_name': 'Portail - Catégorie ',
                'verbose_name_plural': 'Portail - Catégories',
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='AppItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Titre')),
                ('internal_url', models.CharField(blank=True, help_text="URL pour l'accès en interne (Laisser vide si c'est la même que celle pour l'accès externe).", max_length=250, null=True, verbose_name='URL interne')),
                ('external_url', models.CharField(blank=True, help_text="URL pour l'accès depuis l'extérieur (Laisser vide si pas d'accès possible)", max_length=250, null=True, verbose_name='URL externe')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'ordering': ['desktop_config__category', 'desktop_config__rank', 'title'],
            },
        ),
        migrations.CreateModel(
            name='TabletAppConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tablet_title', models.CharField(blank=True, help_text="Si différent du titre de l'application", max_length=100, null=True, verbose_name='Titre sur tablette')),
                ('color', models.CharField(blank=True, max_length=10, null=True, verbose_name='Couleur de fond')),
                ('textColor', models.CharField(blank=True, max_length=10, null=True, verbose_name='Couleur du texte')),
                ('icon', models.FileField(blank=True, help_text='Fichier SVG de préférence', max_length=250, upload_to='icons', verbose_name='Icône')),
                ('info', models.TextField(blank=True, help_text="S'afficheront dans un fenêtre de dialogue en touchant une icône ⓘ", null=True, verbose_name='Informations')),
                ('parent_app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tablet_config', to='nav.appitem')),
            ],
        ),
        migrations.CreateModel(
            name='TabletProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(blank=True, help_text='Lien à utiliser pour accéder à ce profil (ex : mon-profil)', max_length=20, null=True, unique=True, verbose_name='URL')),
                ('title', models.CharField(max_length=50, verbose_name='Titre')),
                ('dark_theme', models.BooleanField(default=False, verbose_name='Thème sombre')),
            ],
            options={
                'verbose_name': 'Tablette - Profil',
                'verbose_name_plural': 'Tablette - Profils',
            },
        ),
        migrations.CreateModel(
            name='TabletProfileMapping',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, help_text="'*' pour indiquer un profil par défaut globalement.", max_length=20, null=True, verbose_name='Adresse IP')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mappings', to='nav.tabletprofile', verbose_name='Profil')),
            ],
            options={
                'verbose_name': 'Tablette - Mapping Profil-IP',
            },
        ),
        migrations.CreateModel(
            name='DesktopAppConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_on_portal', models.BooleanField(default=True, verbose_name='Afficher sur le portail')),
                ('rank', models.PositiveIntegerField(default=0, help_text='Rang de cette app dans sa catégorie', verbose_name='Ordre')),
                ('description', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('screencap', models.ImageField(blank=True, max_length=250, upload_to='screencaps', verbose_name="Capture d'écran")),
                ('extra', models.TextField(blank=True, null=True, verbose_name='Contenu extra')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nav.appcategory', verbose_name='Catégorie')),
                ('parent_app', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='desktop_config', to='nav.appitem')),
            ],
            options={
                'ordering': ['category', 'rank', 'parent_app__title'],
            },
        ),
        migrations.CreateModel(
            name='TabletGridItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.PositiveIntegerField(default=0, verbose_name='Rangée')),
                ('col', models.PositiveIntegerField(default=0, verbose_name='Colonne')),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='grid', to='nav.tabletappconfig')),
                ('profile', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='layout', to='nav.tabletprofile')),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Disposition',
                'ordering': ['row', 'col'],
                'unique_together': {('row', 'col', 'profile')},
            },
        ),
    ]
