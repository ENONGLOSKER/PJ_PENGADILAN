# Generated by Django 4.1.4 on 2023-04-14 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absenapp', '0015_alter_absenmodel_pegawai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenmodel',
            name='status',
            field=models.CharField(choices=[('HADIR', 'HADIR'), ('IZIN', 'IZIN'), ('PULANG', 'PULANG'), ('CUTI', 'CUTI')], default='HADIR', max_length=50),
        ),
    ]
