# Generated by Django 4.1.7 on 2023-04-28 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absenapp', '0016_alter_absenmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='absenmodel',
            name='foto',
            field=models.ImageField(blank=True, default='', null=True, upload_to=''),
        ),
    ]