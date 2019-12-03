# Generated by Django 2.2.6 on 2019-10-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Fatura',
                'verbose_name_plural': 'Faturas',
            },
        ),
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descrição'),
        ),
    ]