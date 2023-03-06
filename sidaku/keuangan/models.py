from django.db import models
import os

from koperasi.models import KoperasiModel
from umkmdata.models import UmkmModel



class KeuanganModel(models.Model):

    def documents_upto(self, instance=None):
        if instance:
            return os.path.join("koperasi", "keuangan", instance)
        return None

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


    doc_nmkop       = models.ForeignKey(KoperasiModel, default=1, on_delete=models.SET_DEFAULT)
    doc_bulan       = models.PositiveIntegerField(choices=LIST_BULAN)
    doc_tahun       = models.IntegerField()
    doc_labrug      = models.FileField(upload_to=documents_upto)
    doc_neraca      = models.FileField(upload_to=documents_upto)
    doc_aruskas     = models.FileField(upload_to=documents_upto)
    doc_permodal    = models.FileField(upload_to=documents_upto)
    doc_catlapkeu   = models.FileField(upload_to=documents_upto)

    lpk_asetprod    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_totaset     = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_pnjmberi    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_astliquid   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_wjblncar    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_shupjk      = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_totmdlsdr   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_ptsneto     = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_bbnperkop   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_bbnusaha    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_biayaoper   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_pendoper    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_shukotor    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_pjmanggta   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_totpiutng   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_pjmbmslh    = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_cadrisk     = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_kasbank     = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_danain      = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_asetlancr   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_asetthnlalu = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_dninthnlalu = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_modalthnlalu= models.BigIntegerField(null=True, blank=True, default=0)
    lpk_hasilthnlalu= models.BigIntegerField(null=True, blank=True, default=0)
    lpk_pendutama   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_totalpendt  = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_simppokok   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_simpwajib   = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_simpanggtin = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_totalsimpin = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_modtimbang  = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_atmr        = models.BigIntegerField(null=True, blank=True, default=0)
    lpk_modpinjanggt= models.BigIntegerField(null=True, blank=True, default=0)
    lpk_wjbjngkapjg = models.BigIntegerField(null=True, blank=True, default=0)

    # lps_kas         = models.BigIntegerField(null=True, blank=True)
    # lps_bank        = models.BigIntegerField(null=True, blank=True)
    # lps_pinjang     = models.BigIntegerField(null=True, blank=True)
    # lps_pinjcet     = models.BigIntegerField(null=True, blank=True)
    # lps_pendrima    = models.BigIntegerField(null=True, blank=True)
    # lps_bbmuka      = models.BigIntegerField(null=True, blank=True)
    # lps_piutagih    = models.BigIntegerField(null=True, blank=True)
    # lps_aslancar    = models.BigIntegerField(null=True, blank=True)
    # lps_persdbrg    = models.BigIntegerField(null=True, blank=True)
    # lps_persdkon    = models.BigIntegerField(null=True, blank=True)
    # lps_piusha      = models.BigIntegerField(null=True, blank=True)
    # lps_tanah       = models.BigIntegerField(null=True, blank=True)
    # lps_bngn        = models.BigIntegerField(null=True, blank=True)
    # lps_akpbngn     = models.BigIntegerField(null=True, blank=True)
    # lps_invenkntr   = models.BigIntegerField(null=True, blank=True)
    # lps_akpinvkntr  = models.BigIntegerField(null=True, blank=True)
    # lps_astdklcr    = models.BigIntegerField(null=True, blank=True)

    # lpk_simpsuk     = models.BigIntegerField(null=True, blank=True)
    # lpk_simpberj    = models.BigIntegerField(null=True, blank=True)
    # lpk_hutush      = models.BigIntegerField(null=True, blank=True)
    # lpk_bbymbyr     = models.BigIntegerField(null=True, blank=True)
    # lpk_hutlain     = models.BigIntegerField(null=True, blank=True)

    # lpe_simppkk     = models.BigIntegerField(null=True, blank=True)
    # lpe_simpwjb     = models.BigIntegerField(null=True, blank=True)
    # lpe_donasi      = models.BigIntegerField(null=True, blank=True)
    # lpe_cadresk     = models.BigIntegerField(null=True, blank=True)
    # lpe_modpnyt     = models.BigIntegerField(null=True, blank=True)


    # lpp_pendjas     = models.BigIntegerField(null=True, blank=True)
    # lpp_pendadm     = models.BigIntegerField(null=True, blank=True)
    # lpp_pendtko     = models.BigIntegerField(null=True, blank=True)
    # lpp_pendlain    = models.BigIntegerField(null=True, blank=True)

    # lpb_bilanghpp   = models.BigIntegerField(null=True, blank=True)
    # lpb_jasimp      = models.BigIntegerField(null=True, blank=True)
    # lpb_jasbank     = models.BigIntegerField(null=True, blank=True)
    # lpb_jasimplain  = models.BigIntegerField(null=True, blank=True)
    # lpb_jasimpjang  = models.BigIntegerField(null=True, blank=True)
    # lpb_jasimpkhus  = models.BigIntegerField(null=True, blank=True)
    # lpb_bypiutang   = models.BigIntegerField(null=True, blank=True)
    # lpb_byasuran    = models.BigIntegerField(null=True, blank=True)
    # lpb_byaudit     = models.BigIntegerField(null=True, blank=True)
    # lpb_bypajak     = models.BigIntegerField(null=True, blank=True)
    # lpb_bykeulain   = models.BigIntegerField(null=True, blank=True)
    # lpb_byrptpeng   = models.BigIntegerField(null=True, blank=True)
    # lpb_byrptangg   = models.BigIntegerField(null=True, blank=True)
    # lpb_byjaladin   = models.BigIntegerField(null=True, blank=True)
    # lpb_bydiklat    = models.BigIntegerField(null=True, blank=True)
    # lpb_honorpeng   = models.BigIntegerField(null=True, blank=True)
    # lpb_bypmbina    = models.BigIntegerField(null=True, blank=True)
    # lpb_byorglain   = models.BigIntegerField(null=True, blank=True)
    # lpb_gjkaryawan  = models.BigIntegerField(null=True, blank=True)
    # lpb_tunjangan   = models.BigIntegerField(null=True, blank=True)
    # lpb_konsumsi    = models.BigIntegerField(null=True, blank=True)
    # lpb_bytransdin  = models.BigIntegerField(null=True, blank=True)
    # lpb_bypend      = models.BigIntegerField(null=True, blank=True)
    # lpb_bykarylain  = models.BigIntegerField(null=True, blank=True)
    # lpb_byatulis    = models.BigIntegerField(null=True, blank=True)
    # lpb_bylistrik   = models.BigIntegerField(null=True, blank=True)
    # lpb_bytelp      = models.BigIntegerField(null=True, blank=True)
    # lpb_byair       = models.BigIntegerField(null=True, blank=True)
    # lpb_byopslain   = models.BigIntegerField(null=True, blank=True)

    created_by      = models.CharField(max_length=25,blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=25,blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "lapkeu-" + self.doc_nmkop

    class Meta:
        db_table = 'keuangan_kop_data'
        verbose_name_plural = 'keuangan_kop_data'



class KeuanganUMKMModel(models.Model):

    def documents_upto(self, instance=None):
        if instance:
            return os.path.join("umkm", "keuangan", instance)
        return None

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


    doc_nmumkm       = models.ForeignKey(UmkmModel, default=1, on_delete=models.SET_DEFAULT)
    doc_bulan       = models.PositiveIntegerField(choices=LIST_BULAN)
    doc_tahun       = models.IntegerField()
    doc_labrug      = models.FileField(upload_to=documents_upto)
    doc_neraca      = models.FileField(upload_to=documents_upto)
    doc_aruskas     = models.FileField(upload_to=documents_upto)
    doc_permodal    = models.FileField(upload_to=documents_upto)
    doc_catlapkeu   = models.FileField(upload_to=documents_upto)


    lps_kas         = models.BigIntegerField(null=True, blank=True)
    lps_bank        = models.BigIntegerField(null=True, blank=True)
    lps_pinjang     = models.BigIntegerField(null=True, blank=True)
    lps_pinjcet     = models.BigIntegerField(null=True, blank=True)
    lps_pendrima    = models.BigIntegerField(null=True, blank=True)
    lps_bbmuka      = models.BigIntegerField(null=True, blank=True)
    lps_piutagih    = models.BigIntegerField(null=True, blank=True)
    lps_aslancar    = models.BigIntegerField(null=True, blank=True)
    lps_persdbrg    = models.BigIntegerField(null=True, blank=True)
    lps_persdkon    = models.BigIntegerField(null=True, blank=True)
    lps_piusha      = models.BigIntegerField(null=True, blank=True)
    lps_tanah       = models.BigIntegerField(null=True, blank=True)
    lps_bngn        = models.BigIntegerField(null=True, blank=True)
    lps_akpbngn     = models.BigIntegerField(null=True, blank=True)
    lps_invenkntr   = models.BigIntegerField(null=True, blank=True)
    lps_akpinvkntr  = models.BigIntegerField(null=True, blank=True)
    lps_astdklcr    = models.BigIntegerField(null=True, blank=True)

    lpk_simpsuk     = models.BigIntegerField(null=True, blank=True)
    lpk_simpberj    = models.BigIntegerField(null=True, blank=True)
    lpk_hutush      = models.BigIntegerField(null=True, blank=True)
    lpk_bbymbyr     = models.BigIntegerField(null=True, blank=True)
    lpk_hutlain     = models.BigIntegerField(null=True, blank=True)

    lpe_simppkk     = models.BigIntegerField(null=True, blank=True)
    lpe_simpwjb     = models.BigIntegerField(null=True, blank=True)
    lpe_donasi      = models.BigIntegerField(null=True, blank=True)
    lpe_cadresk     = models.BigIntegerField(null=True, blank=True)
    lpe_modpnyt     = models.BigIntegerField(null=True, blank=True)


    lpp_pendjas     = models.BigIntegerField(null=True, blank=True)
    lpp_pendadm     = models.BigIntegerField(null=True, blank=True)
    lpp_pendtko     = models.BigIntegerField(null=True, blank=True)
    lpp_pendlain    = models.BigIntegerField(null=True, blank=True)

    lpb_bilanghpp   = models.BigIntegerField(null=True, blank=True)
    lpb_jasimp      = models.BigIntegerField(null=True, blank=True)
    lpb_jasbank     = models.BigIntegerField(null=True, blank=True)
    lpb_jasimplain  = models.BigIntegerField(null=True, blank=True)
    lpb_jasimpjang  = models.BigIntegerField(null=True, blank=True)
    lpb_jasimpkhus  = models.BigIntegerField(null=True, blank=True)
    lpb_bypiutang   = models.BigIntegerField(null=True, blank=True)
    lpb_byasuran    = models.BigIntegerField(null=True, blank=True)
    lpb_byaudit     = models.BigIntegerField(null=True, blank=True)
    lpb_bypajak     = models.BigIntegerField(null=True, blank=True)
    lpb_bykeulain   = models.BigIntegerField(null=True, blank=True)
    lpb_byrptpeng   = models.BigIntegerField(null=True, blank=True)
    lpb_byrptangg   = models.BigIntegerField(null=True, blank=True)
    lpb_byjaladin   = models.BigIntegerField(null=True, blank=True)
    lpb_bydiklat    = models.BigIntegerField(null=True, blank=True)
    lpb_honorpeng   = models.BigIntegerField(null=True, blank=True)
    lpb_bypmbina    = models.BigIntegerField(null=True, blank=True)
    lpb_byorglain   = models.BigIntegerField(null=True, blank=True)
    lpb_gjkaryawan  = models.BigIntegerField(null=True, blank=True)
    lpb_tunjangan   = models.BigIntegerField(null=True, blank=True)
    lpb_konsumsi    = models.BigIntegerField(null=True, blank=True)
    lpb_bytransdin  = models.BigIntegerField(null=True, blank=True)
    lpb_bypend      = models.BigIntegerField(null=True, blank=True)
    lpb_bykarylain  = models.BigIntegerField(null=True, blank=True)
    lpb_byatulis    = models.BigIntegerField(null=True, blank=True)
    lpb_bylistrik   = models.BigIntegerField(null=True, blank=True)
    lpb_bytelp      = models.BigIntegerField(null=True, blank=True)
    lpb_byair       = models.BigIntegerField(null=True, blank=True)
    lpb_byopslain   = models.BigIntegerField(null=True, blank=True)

    created_by      = models.CharField(max_length=25,blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=25,blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now=True)


    def __str__(self):
        return "lapkeu-" + str(self.doc_nmumkm)

    class Meta:
        db_table = 'keuangan_umkm_data'
        verbose_name_plural = 'keuangan_umkm_data'

