# Generated by Django 4.1.4 on 2022-12-20 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_foodcategories_dish'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coreuser',
            name='age',
        ),
        migrations.RemoveField(
            model_name='coreuser',
            name='phone',
        ),
    ]