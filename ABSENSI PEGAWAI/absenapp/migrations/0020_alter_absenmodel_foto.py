# Generated by Django 4.1.7 on 2023-04-28 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absenapp', '0019_alter_absenmodel_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absenmodel',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]