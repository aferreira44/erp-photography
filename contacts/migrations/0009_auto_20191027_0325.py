# Generated by Django 2.2.6 on 2019-10-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_auto_20191027_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(blank=True,
                                   max_length=200,
                                   null=True,
                                   verbose_name='Nome do meio'),
        ),
    ]
