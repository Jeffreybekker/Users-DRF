# Generated by Django 5.1.3 on 2024-12-01 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0013_alter_artists_artistsid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artists',
            name='artistsID',
        ),
        migrations.AddField(
            model_name='artists',
            name='id',
            field=models.BigAutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
