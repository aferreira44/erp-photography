# Generated by Django 2.2.6 on 2019-10-27 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0004_service_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='services',
            field=models.ManyToManyField(to='sales.Service'),
        ),
    ]
