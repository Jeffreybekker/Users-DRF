# Generated by Django 5.1.3 on 2024-12-01 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gebruikersAPI', '0005_alter_user_city'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Artist',
        ),
    ]