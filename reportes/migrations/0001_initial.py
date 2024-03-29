# Generated by Django 4.2.1 on 2023-07-28 13:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('productos', '0001_initial'),
        ('ventas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Codigo')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('igtf', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Factura',
                'verbose_name_plural': 'Facturas',
                'db_table': 'Factura',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='Nota_de_entrega',
            fields=[
                ('codigo', models.CharField(max_length=5, primary_key=True, serialize=False, unique=True, verbose_name='Codigo')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientes.cliente')),
            ],
            options={
                'verbose_name': 'Nota_de_entrega',
                'verbose_name_plural': 'Notas_de_entregas',
                'db_table': 'Nota_de_entrega',
                'ordering': ['codigo'],
            },
        ),
        migrations.CreateModel(
            name='MN_NotaDeEntrega_Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('nota_de_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.nota_de_entrega')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'MN_NotaDeEntrega_Producto',
                'verbose_name_plural': 'MN_NotasDeEntregas_Productos',
                'db_table': 'MN_NotaDeEntrega_Producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MN_NotaDeEntrega_MetodoDePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('metodo_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.metodo_de_pago')),
                ('nota_de_entrega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.nota_de_entrega')),
            ],
            options={
                'verbose_name': 'MN_NotaDeEntrega_MetodoDePago',
                'verbose_name_plural': 'MN_NotasDeEntregas_MetodosDePagos',
                'db_table': 'MN_NotaDeEntrega_MetodoDePago',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MN_Factura_Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.factura')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productos.producto')),
            ],
            options={
                'verbose_name': 'MN_Factura_Producto',
                'verbose_name_plural': 'MN_Factura_Producto',
                'db_table': 'MN_Factura_Producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MN_Factura_MetodoDePago',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('factura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.factura')),
                ('metodo_de_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ventas.metodo_de_pago')),
            ],
            options={
                'verbose_name': 'MN_Factura_MetodoDePago',
                'verbose_name_plural': 'MN_Facturas_MetodosDePagos',
                'db_table': 'MN_Factura_MetodoDePago',
                'ordering': ['id'],
            },
        ),
    ]
