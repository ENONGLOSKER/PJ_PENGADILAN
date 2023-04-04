# Generated by Django 4.1.7 on 2023-03-29 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jadwal', '0003_alter_jadwal_tgl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jadwal',
            old_name='pihak',
            new_name='penggugat',
        ),
        migrations.AddField(
            model_name='jadwal',
            name='tergugat',
            field=models.CharField(default='tergugat', max_length=50),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='noPerkara',
            field=models.CharField(default='0001/Pdt.G/2023/PA.Sel', max_length=50),
        ),
        migrations.AlterField(
            model_name='jadwal',
            name='ruangan',
            field=models.CharField(choices=[('Ruang Sidang Utama', 'Ruang Sidang Utama'), ('Ruang Sidang Dua', 'Ruang Sidang Dua')], max_length=50),
        ),
    ]
