# Generated by Django 3.1 on 2020-08-27 08:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='listIng_id',
            new_name='listing_id',
        ),
    ]