# Generated by Django 2.2.6 on 2019-10-27 02:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_client_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.Address', verbose_name='Endereço'),
        ),
    ]
