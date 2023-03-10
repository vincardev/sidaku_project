# Generated by Django 4.1 on 2023-03-04 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produk', '0007_rename_harga_detpenilaiansupp_dps_harga_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detdemandprod',
            name='dpd_bulan',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Januari'), (2, 'Februari'), (3, 'Maret'), (4, 'April'), (5, 'Mei'), (6, 'Juni'), (7, 'Juli'), (8, 'Agustus'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'Desember')], null=True),
        ),
        migrations.AlterField(
            model_name='detdemandprod',
            name='dpd_demand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detdemandprod',
            name='dpd_nmprod',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='detdemandprod',
            name='dpd_produksi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detdemandprod',
            name='dpd_tahun',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detdemandsup',
            name='dsp_bulan',
            field=models.PositiveIntegerField(blank=True, choices=[(1, 'Januari'), (2, 'Februari'), (3, 'Maret'), (4, 'April'), (5, 'Mei'), (6, 'Juni'), (7, 'Juli'), (8, 'Agustus'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'Desember')], null=True),
        ),
        migrations.AlterField(
            model_name='detdemandsup',
            name='dsp_demand',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detdemandsup',
            name='dsp_jensup',
            field=models.CharField(blank=True, choices=[('retail', 'Retail'), ('pemasok', 'Pemasok')], max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='detdemandsup',
            name='dsp_produksi',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detdemandsup',
            name='dsp_tahun',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='detpenilaiansupp',
            name='dps_kualitas',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detpenilaiansupp',
            name='dps_nm_supp',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='detpenilaiansupp',
            name='dps_pengiriman',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='produkmodel',
            name='harga',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produkmodel',
            name='komoditi',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='produkmodel',
            name='satuan',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='produkmodel',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produkmodel',
            name='volume',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='produkumkm',
            name='harga',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produkumkm',
            name='komoditi',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='produkumkm',
            name='satuan',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='produkumkm',
            name='total',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='produkumkm',
            name='volume',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
