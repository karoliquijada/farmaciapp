# Generated by Django 4.2.3 on 2023-07-29 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='exento',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='producto',
            name='fecha_de_vencimiento',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Fecha'),
        ),
    ]
