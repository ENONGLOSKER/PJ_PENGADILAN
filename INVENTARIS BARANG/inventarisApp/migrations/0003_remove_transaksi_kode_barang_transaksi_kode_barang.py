# Generated by Django 4.1.5 on 2023-04-09 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventarisApp', '0002_rename_kategori_katagori'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaksi',
            name='kode_barang',
        ),
        migrations.AddField(
            model_name='transaksi',
            name='Kode_barang',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.DO_NOTHING, to='inventarisApp.katagori'),
        ),
    ]
