# Generated by Django 5.1.3 on 2024-12-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0007_remove_artist_id_artist_artistid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='artistID',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
