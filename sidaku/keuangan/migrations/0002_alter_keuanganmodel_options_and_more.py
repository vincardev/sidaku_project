# Generated by Django 4.1 on 2022-11-16 07:52

from django.db import migrations, models
import django.db.models.deletion
import keuangan.models


class Migration(migrations.Migration):

    dependencies = [
        ('umkmdata', '0002_rename_dtu_totalthn_umkmmodel_dtu_totalaset'),
        ('keuangan', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='keuanganmodel',
            options={'verbose_name_plural': 'keuangan_kop_data'},
        ),
        migrations.AlterModelTable(
            name='keuanganmodel',
            table='keuangan_kop_data',
        ),
        migrations.CreateModel(
            name='KeuanganUMKMModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doc_bulan', models.PositiveIntegerField(choices=[(1, 'Januari'), (2, 'Februari'), (3, 'Maret'), (4, 'April'), (5, 'Mei'), (6, 'Juni'), (7, 'Juli'), (8, 'Agustus'), (9, 'September'), (10, 'Oktober'), (11, 'November'), (12, 'Desember')])),
                ('doc_tahun', models.IntegerField()),
                ('doc_labrug', models.FileField(upload_to=keuangan.models.KeuanganUMKMModel.documents_upto)),
                ('doc_neraca', models.FileField(upload_to=keuangan.models.KeuanganUMKMModel.documents_upto)),
                ('doc_aruskas', models.FileField(upload_to=keuangan.models.KeuanganUMKMModel.documents_upto)),
                ('doc_permodal', models.FileField(upload_to=keuangan.models.KeuanganUMKMModel.documents_upto)),
                ('doc_catlapkeu', models.FileField(upload_to=keuangan.models.KeuanganUMKMModel.documents_upto)),
                ('lps_kas', models.BigIntegerField(blank=True, null=True)),
                ('lps_bank', models.BigIntegerField(blank=True, null=True)),
                ('lps_pinjang', models.BigIntegerField(blank=True, null=True)),
                ('lps_pinjcet', models.BigIntegerField(blank=True, null=True)),
                ('lps_pendrima', models.BigIntegerField(blank=True, null=True)),
                ('lps_bbmuka', models.BigIntegerField(blank=True, null=True)),
                ('lps_piutagih', models.BigIntegerField(blank=True, null=True)),
                ('lps_aslancar', models.BigIntegerField(blank=True, null=True)),
                ('lps_persdbrg', models.BigIntegerField(blank=True, null=True)),
                ('lps_persdkon', models.BigIntegerField(blank=True, null=True)),
                ('lps_piusha', models.BigIntegerField(blank=True, null=True)),
                ('lps_tanah', models.BigIntegerField(blank=True, null=True)),
                ('lps_bngn', models.BigIntegerField(blank=True, null=True)),
                ('lps_akpbngn', models.BigIntegerField(blank=True, null=True)),
                ('lps_invenkntr', models.BigIntegerField(blank=True, null=True)),
                ('lps_akpinvkntr', models.BigIntegerField(blank=True, null=True)),
                ('lps_astdklcr', models.BigIntegerField(blank=True, null=True)),
                ('lpk_simpsuk', models.BigIntegerField(blank=True, null=True)),
                ('lpk_simpberj', models.BigIntegerField(blank=True, null=True)),
                ('lpk_hutush', models.BigIntegerField(blank=True, null=True)),
                ('lpk_bbymbyr', models.BigIntegerField(blank=True, null=True)),
                ('lpk_hutlain', models.BigIntegerField(blank=True, null=True)),
                ('lpe_simppkk', models.BigIntegerField(blank=True, null=True)),
                ('lpe_simpwjb', models.BigIntegerField(blank=True, null=True)),
                ('lpe_donasi', models.BigIntegerField(blank=True, null=True)),
                ('lpe_cadresk', models.BigIntegerField(blank=True, null=True)),
                ('lpe_modpnyt', models.BigIntegerField(blank=True, null=True)),
                ('lpp_pendjas', models.BigIntegerField(blank=True, null=True)),
                ('lpp_pendadm', models.BigIntegerField(blank=True, null=True)),
                ('lpp_pendtko', models.BigIntegerField(blank=True, null=True)),
                ('lpp_pendlain', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bilanghpp', models.BigIntegerField(blank=True, null=True)),
                ('lpb_jasimp', models.BigIntegerField(blank=True, null=True)),
                ('lpb_jasbank', models.BigIntegerField(blank=True, null=True)),
                ('lpb_jasimplain', models.BigIntegerField(blank=True, null=True)),
                ('lpb_jasimpjang', models.BigIntegerField(blank=True, null=True)),
                ('lpb_jasimpkhus', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bypiutang', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byasuran', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byaudit', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bypajak', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bykeulain', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byrptpeng', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byrptangg', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byjaladin', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bydiklat', models.BigIntegerField(blank=True, null=True)),
                ('lpb_honorpeng', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bypmbina', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byorglain', models.BigIntegerField(blank=True, null=True)),
                ('lpb_gjkaryawan', models.BigIntegerField(blank=True, null=True)),
                ('lpb_tunjangan', models.BigIntegerField(blank=True, null=True)),
                ('lpb_konsumsi', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bytransdin', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bypend', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bykarylain', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byatulis', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bylistrik', models.BigIntegerField(blank=True, null=True)),
                ('lpb_bytelp', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byair', models.BigIntegerField(blank=True, null=True)),
                ('lpb_byopslain', models.BigIntegerField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=25, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_by', models.CharField(blank=True, max_length=25, null=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('doc_nmumkm', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='umkmdata.umkmmodel')),
            ],
            options={
                'verbose_name_plural': 'keuangan_umkm_data',
                'db_table': 'keuangan_umkm_data',
            },
        ),
    ]
