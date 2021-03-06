# Generated by Django 2.2.6 on 2019-12-03 01:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0009_auto_20191203_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='products',
        ),
        migrations.RemoveField(
            model_name='invoice',
            name='services',
        ),
        migrations.AddField(
            model_name='invoiceproduct',
            name='invoice',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='sales.Invoice',
                verbose_name='Fatura'),
        ),
        migrations.AddField(
            model_name='invoiceservice',
            name='invoice',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to='sales.Invoice',
                verbose_name='Fatura'),
        ),
    ]
