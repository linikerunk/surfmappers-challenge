# Generated by Django 2.2.7 on 2020-10-16 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20201015_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeryphoto',
            name='approved',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Aprovado'),
        ),
    ]
