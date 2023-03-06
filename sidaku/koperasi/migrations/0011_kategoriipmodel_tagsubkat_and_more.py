# Generated by Django 4.1 on 2023-02-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('koperasi', '0010_detaildppatuh'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategoriipmodel',
            name='tagsubkat',
            field=models.CharField(blank=True, choices=[('', ''), ('risiko-inheren', 'RISIKO INHEREN '), ('kualitas-manajemen-risiko', 'KUALITAS PENERAPAN MANAJEMEN RISIKO'), ('evaluasi-kinerja-keuangan', 'EVALUASI KINERJA KEUANGAN'), ('manajemen-keuangan', 'MANAJEMEN KEUANGAN'), ('kesinambungan-keuangan', 'KESINAMBUNGAN KEUANGAN'), ('kualitas-manajemen-risiko', 'KUALITAS PENERAPAN MANAJEMEN RISIKO'), ('kecukupan-modal', 'KECUKUPAN PERMODALAN'), ('kecukupan-pengelolaan-modal', 'KECUKUPAN PENGELOLAAN PERMODALAN')], default='', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kategoriipmodel',
            name='ipkat',
            field=models.CharField(blank=True, choices=[('tata-kelola', 'TATA KELOLA'), ('profil-risiko', 'PROFIL RISIKO'), ('kinerja', 'KINERJA'), ('permodalan', 'PERMODALAN')], default='tata-kelola', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='kategoriipmodel',
            name='ipsubkat',
            field=models.CharField(blank=True, choices=[('prinsip-koperasi', 'PRINSIP KOPERASI'), ('kelembagaan', 'KELEMBAGAAN'), ('manajemen', 'MANAJEMEN'), ('risiko-operasional', 'Risiko Operasional'), ('risiko-kepatuhan', 'Risiko Kepatuhan'), ('risiko-likuiditas', 'Risiko Likuiditas'), ('kpmr-pinjaman', 'Kualitas Penerapan Manajemen Risiko Pinjaman/pembiayaan'), ('kpmr-operasional', 'Kualitas Penerapan Manajemen Risiko Operasional'), ('kpmr-kepatuhan', 'Kualitas Penerapan Manajemen Risiko Kepatuhan'), ('kpmr-likuiditas', 'Kualitas Penerapan Manajemen Risiko Likuiditas'), ('rentabilitas-kemandirian', 'Rentabilitas dan Kemandirian'), ('efisiensi', 'Efisiensi'), ('kualitas-aset', 'Kualitas Aset'), ('aspek-likuiditas', 'Aspek Likuiditas'), ('pertumbuhan', 'Pertumbuhan'), ('aspek-jatidiri', 'Aspek Jatidiri')], default='prinsip-koperasi', max_length=200, null=True),
        ),
    ]