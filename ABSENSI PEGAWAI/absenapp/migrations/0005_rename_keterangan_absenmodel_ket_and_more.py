# Generated by Django 4.1.7 on 2023-02-26 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('absenapp', '0004_alter_absenmodel_jabatan_alter_absenmodel_tgl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='absenmodel',
            old_name='keterangan',
            new_name='ket',
        ),
        migrations.RemoveField(
            model_name='absenmodel',
            name='bidang',
        ),
        migrations.RemoveField(
            model_name='absenmodel',
            name='foto',
        ),
        migrations.RemoveField(
            model_name='absenmodel',
            name='jabatan',
        ),
        migrations.RemoveField(
            model_name='absenmodel',
            name='nama',
        ),
        migrations.RemoveField(
            model_name='absenmodel',
            name='nip',
        ),
        migrations.CreateModel(
            name='profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nip', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='')),
                ('bidang', models.CharField(max_length=50)),
                ('jabatan', models.CharField(max_length=50, null=True)),
                ('nama', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
