# Generated by Django 4.1.5 on 2023-03-25 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal', '0002_alter_jadwal_pihak_delete_pengguna'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='tgl',
            field=models.DateTimeField(),
        ),
    ]
