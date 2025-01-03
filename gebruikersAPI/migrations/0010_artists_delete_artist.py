# Generated by Django 5.1.3 on 2024-12-01 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0009_remove_artist_artistid_artist_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('artistID', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Artist',
        ),
    ]
