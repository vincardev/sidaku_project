from django.db import models

from koperasi.models import KoperasiModel
from umkmdata.models import UmkmModel


Jan     = 1
Feb     = 2
Mar     = 3
Apr     = 4
Mei     = 5
Jun     = 6
Jul     = 7
Aug     = 8
Sep     = 9
Oct     = 10
Nov     = 11
Dec     = 12

LIST_BULAN = [
    (Jan, ("Januari")),
    (Feb, ("Februari")),
    (Mar, ("Maret")),
    (Apr, ("April")),
    (Mei, ("Mei")),
    (Jun, ("Juni")),
    (Jul, ("Juli")),
    (Aug, ("Agustus")),
    (Sep, ("September")),
    (Oct, ("Oktober")),
    (Nov, ("November")),
    (Dec, ("Desember")),
]

ret     = 'retail'
supp    = 'pemasok'

LIST_JEN_SUPP = [
    (ret, ("Retail")),
    (supp, ("Pemasok"))
]

class ProdukModel(models.Model):
    komoditi      = models.CharField(max_length=150, blank=True, null=True)
    volume        = models.CharField(max_length=150, blank=True, null=True)
    satuan        = models.CharField(max_length=150, blank=True, null=True)
    harga         = models.IntegerField(default=0, blank=True, null=True)
    total         = models.IntegerField(default=0, blank=True, null=True)
    fotoprod      = models.ImageField(upload_to= 'produk/', null=True, blank=True)
    kopid         = models.ForeignKey(KoperasiModel, on_delete=models.CASCADE, null = True, blank = True )

    class Meta:
        db_table = 'produk_kop'
        verbose_name_plural = 'produk_kop'

    def __str__(self):
        return self.komoditi


class ProdukUMKM(models.Model):
    komoditi      = models.CharField(max_length=150, blank=True, null=True)
    volume        = models.CharField(max_length=150, blank=True, null=True)
    satuan        = models.CharField(max_length=150, blank=True, null=True)
    harga         = models.IntegerField(default=0, blank=True, null=True)
    total         = models.IntegerField(default=0, blank=True, null=True)
    fotoprod      = models.ImageField(upload_to= 'produk/', null=True, blank=True)
    umkmid        = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    class Meta:
        db_table = 'produk_umkm'
        verbose_name_plural = 'produk_umkm'

    def __str__(self):
        return self.komoditi



class DetDemandProd(models.Model):
    dpd_nmprod    = models.CharField(max_length=150, blank=True, null=True)
    dpd_bulan     = models.PositiveIntegerField(choices=LIST_BULAN, blank=True, null=True)
    dpd_tahun     = models.IntegerField(default=0)
    dpd_demand    = models.IntegerField(default=0)
    dpd_produksi  = models.IntegerField(default=0)
    umkmid        = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    
    class Meta:
        db_table = 'det_demand_prod'
        verbose_name_plural = 'det_demand_prod'

    def __str__(self):
        return self.dpd_nmprod


class DetDemandSup(models.Model):
    dsp_jensup    = models.CharField(choices=LIST_JEN_SUPP, max_length=150, blank=True, null=True )
    dsp_bulan     = models.PositiveIntegerField(choices=LIST_BULAN, blank=True, null=True)
    dsp_tahun     = models.IntegerField(default=0)
    dsp_demand    = models.IntegerField(default=0)
    dsp_produksi  = models.IntegerField(default=0)
    umkmid      = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    
    class Meta:
        db_table = 'det_demand_supp'
        verbose_name_plural = 'det_demand_supp'

    def __str__(self):
        return self.dsp_jensup



class DetPenilaianSupp(models.Model):
    dps_nm_supp         = models.CharField(max_length=200, blank=True, null=True)
    dps_kualitas        = models.CharField(max_length=200, blank=True, null=True)
    dps_pengiriman      = models.CharField(max_length=200, blank=True, null=True)
    dps_harga           = models.IntegerField()
    umkmid              = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    
    class Meta:
        db_table = 'det_nilai_supp'
        verbose_name_plural = 'det_nilai_supp'

    def __str__(self):
        return self.dps_nm_supp