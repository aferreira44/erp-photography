# Generated by Django 2.2.6 on 2019-10-27 01:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20191027_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Último Nome'),
        ),
    ]
