# Generated by Django 2.2.7 on 2020-10-15 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201015_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeryphoto',
            name='approved',
            field=models.BooleanField(default=False, verbose_name='Aprovado'),
        ),
    ]