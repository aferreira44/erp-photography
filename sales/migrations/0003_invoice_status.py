# Generated by Django 2.2.6 on 2019-10-27 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20191027_0251'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='status',
            field=models.CharField(choices=[('PENDING', 'Pendente'), ('PAID', 'Paga'), ('CANCELED', 'Cancelada'), ('DRAFT', 'Rascunho'), ('PARTIALLY_PAID', 'Parcialmente Paga')], default=('PENDING', 'Pendente'), max_length=50),
        ),
    ]
