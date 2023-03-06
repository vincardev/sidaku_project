# Generated by Django 4.1 on 2022-12-06 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koperasi', '0005_alter_koperasimodel_du_jenkop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='koperasimodel',
            name='du_jenkop',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Konsumen'), (2, 'Simpan Pinjam'), (3, 'Jasa'), (4, 'Produsen'), (5, 'Pemasaran')], default=1, null=True),
        ),
    ]