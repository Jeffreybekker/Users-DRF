# Generated by Django 5.1.3 on 2024-12-01 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0012_rename_artistid_artists_artistsid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artists',
            name='artistsID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
