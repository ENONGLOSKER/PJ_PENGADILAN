# Generated by Django 4.1.5 on 2023-04-09 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventarisApp', '0004_alter_transaksi_kode_barang'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='barang',
            name='id',
        ),
        migrations.AlterField(
            model_name='barang',
            name='Kode_barang',
            field=models.CharField(editable=False, max_length=5, primary_key=True, serialize=False, unique=True),
        ),
    ]
