# Generated by Django 4.1.5 on 2023-04-09 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarisApp', '0003_remove_transaksi_kode_barang_transaksi_kode_barang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaksi',
            name='Kode_barang',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='inventarisApp.barang'),
        ),
    ]
