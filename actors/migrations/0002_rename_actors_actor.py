# Generated by Django 5.1.1 on 2024-09-30 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actors', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actors',
            new_name='Actor',
        ),
    ]
