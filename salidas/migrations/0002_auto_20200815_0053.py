# Generated by Django 2.2.5 on 2020-08-15 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salidas', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='facturadet',
            options={'verbose_name': 'Detalle de Factura', 'verbose_name_plural': 'Detalles de Facturas'},
        ),
        migrations.RenameField(
            model_name='facturaenc',
            old_name='fecha_faactura',
            new_name='fecha_factura',
        ),
        migrations.AddField(
            model_name='facturadet',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='facturadet',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
