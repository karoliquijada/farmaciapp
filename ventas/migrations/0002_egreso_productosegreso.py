# Generated by Django 4.2.3 on 2023-07-29 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_producto_exento_and_more'),
        ('clientes', '0002_alter_cliente_options_remove_cliente_id_and_more'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Egreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pedido', models.DateField(max_length=255)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('pagado', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('comentarios', models.TextField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('ticket', models.BooleanField(default=True)),
                ('desglosar', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now_add=True, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clientee', to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'egreso',
                'verbose_name_plural': 'egresos',
                'order_with_respect_to': 'fecha_pedido',
            },
        ),
        migrations.CreateModel(
            name='ProductosEgreso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.DecimalField(decimal_places=2, max_digits=20)),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('entregado', models.BooleanField(default=True)),
                ('devolucion', models.BooleanField(default=False)),
                ('egreso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.egreso')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'producto egreso',
                'verbose_name_plural': 'productos egreso',
                'order_with_respect_to': 'created',
            },
        ),
    ]
