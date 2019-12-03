# Generated by Django 2.2.6 on 2019-10-27 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20191027_0128'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(max_length=200, verbose_name='Primeiro Nome'),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(max_length=200, verbose_name='Sobrenome'),
        ),
        migrations.AlterField(
            model_name='client',
            name='middle_name',
            field=models.CharField(max_length=200, verbose_name='Nome do meio'),
        ),
    ]
