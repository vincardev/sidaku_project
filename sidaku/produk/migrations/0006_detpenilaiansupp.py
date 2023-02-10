# Generated by Django 4.1 on 2022-11-15 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('umkmdata', '0002_rename_dtu_totalthn_umkmmodel_dtu_totalaset'),
        ('produk', '0005_rename_dpd_umkm_detdemandprod_umkmid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DetPenilaianSupp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nm_supp', models.CharField(max_length=200)),
                ('kualitas', models.CharField(max_length=200)),
                ('pengiriman', models.CharField(max_length=200)),
                ('harga', models.IntegerField()),
                ('umkmid', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='umkmdata.umkmmodel')),
            ],
            options={
                'verbose_name_plural': 'det_nilai_supp',
                'db_table': 'det_nilai_supp',
            },
        ),
    ]