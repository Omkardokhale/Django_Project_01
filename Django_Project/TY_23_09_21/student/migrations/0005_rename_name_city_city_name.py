# Generated by Django 3.2.7 on 2021-09-29 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_country_population'),
    ]

    operations = [
        migrations.RenameField(
            model_name='city',
            old_name='name',
            new_name='city_name',
        ),
    ]
