# Generated by Django 2.2.6 on 2019-10-27 01:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20191027_0035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='born_name',
            new_name='born_date',
        ),
    ]
