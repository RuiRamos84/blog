# Generated by Django 4.1.3 on 2022-11-09 01:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoria',
            name='slug',
        ),
    ]
