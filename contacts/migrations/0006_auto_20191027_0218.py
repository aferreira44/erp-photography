# Generated by Django 2.2.6 on 2019-10-27 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0005_auto_20191027_0150'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='cpf',
            field=models.CharField(default=0,
                                   max_length=11,
                                   verbose_name='CPF'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='rg',
            field=models.CharField(default=0, max_length=14,
                                   verbose_name='RG'),
            preserve_default=False,
        ),
    ]
