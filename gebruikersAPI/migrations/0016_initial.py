# Generated by Django 5.1.3 on 2024-12-01 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('gebruikersAPI', '0015_delete_artists'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
    ]
