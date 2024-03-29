# Generated by Django 4.2.1 on 2023-07-28 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Impuesto',
            fields=[
                ('tipo', models.CharField(max_length=150, primary_key=True, serialize=False, unique=True)),
                ('tasa', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Impuesto',
                'verbose_name_plural': 'Impuestos',
                'db_table': 'Impuesto',
                'ordering': ['tipo'],
            },
        ),
        migrations.CreateModel(
            name='Metodo_de_pago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nombre', models.CharField(max_length=150)),
                ('divisa', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Metodo_de_pago',
                'verbose_name_plural': 'Metodos_de_pagos',
                'db_table': 'Metodo_de_pago',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Tasa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('tasa', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
            ],
            options={
                'verbose_name': 'Tasa',
                'verbose_name_plural': 'Tasas',
                'db_table': 'Tasas',
                'ordering': ['id'],
            },
        ),
    ]
