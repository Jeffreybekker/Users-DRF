# Generated by Django 5.1.3 on 2024-11-26 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0002_user_age_user_city_user_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='city',
            field=models.CharField(default='Culemborg', max_length=100),
        ),
    ]
