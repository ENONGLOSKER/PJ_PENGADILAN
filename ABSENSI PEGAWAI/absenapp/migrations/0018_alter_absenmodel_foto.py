# Generated by Django 4.1.7 on 2023-04-28 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absenapp', '0017_absenmodel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenmodel',
            name='foto',
            field=models.ImageField(blank=True, default='', null=True, upload_to='img'),
        ),
    ]
