# Generated by Django 2.2.6 on 2019-12-03 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0007_auto_20191203_0106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoiceproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Product', verbose_name='Produto'),
        ),
    ]
