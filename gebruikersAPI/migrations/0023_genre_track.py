# Generated by Django 5.1.3 on 2024-12-02 02:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0022_remove_album_artist_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('GenreID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('trackID', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('albumID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gebruikersAPI.album')),
                ('genreID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gebruikersAPI.genre')),
            ],
        ),
    ]