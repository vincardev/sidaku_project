# Generated by Django 4.1 on 2022-11-04 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koperasi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koperasimodel',
            name='rkp_nibkop',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='koperasimodel',
            name='rkp_nikpmlk',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
