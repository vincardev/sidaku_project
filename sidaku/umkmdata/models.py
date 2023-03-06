from django.db import models

from django.template.defaultfilters import slugify
from autoslug import AutoSlugField
# from .models import UserProfile
import os

from userprofile.models import UserProfile

# from .models import ProdukModel



class BidangUsaha(models.Model):
    nama         = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='nama', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'bidang_usaha'
        verbose_name_plural = 'bidang_usaha'

class BentukUsaha(models.Model):
    nama         = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='nama', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.nama

    class Meta:
        db_table = 'bentuk_usaha'
        verbose_name_plural = 'bentuk_usaha'



class UmkmModel(models.Model):

    def profile_upto(self, instance=None):
        if instance:
            return os.path.join("umkm", "profil",instance)
        return None

    def documents_upto(self, instance=None):
        if instance:
            return os.path.join("umkm", "documents", instance)
        return None

    PERO    = 1
    CV      = 2
    UD      = 3
    KOP     = 4
    DLL     = 5

    BENTUK_USAHA = [
        (PERO, ("Perorangan")),
        (CV, ("CV")),
        (UD, ("UD")),
        (KOP, ("Koperasi")),
        (DLL, ("Lainnya"))
    ]

    MADK    = 1
    MIDK    = 2
    KRJ     = 3
    PDG     = 4
    JS      = 5
    LL      = 6

    BIDANG_USAHA = [
        (MADK, ("Makanan dalam Kemasan")),
        (MIDK, ("Minuman dalam Kemasan")),
        (KRJ, ("Kerajinan")),
        (PDG, ("Perdagangan")),
        (JS, ("Jasa")),
        (LL, ("Lainnya")),
    ]


    MKR    = 1
    KCL    = 2
    MNG    = 3

    SKALA_USAHA = [
        (MKR, ("Mikro")),
        (KCL, ("Kecil")),
        (MNG, ("Menengah"))
    ]

    dt_user           = models.ForeignKey(UserProfile, default=1, on_delete=models.SET_DEFAULT)


    pu_noaggta        = models.CharField(max_length=250, null=True, blank=True)
    pu_nmpmlk         = models.CharField(max_length=250)
    pu_aldmisi        = models.TextField(max_length=255)  
    pu_noktp          = models.BigIntegerField()
    pu_notlp          = models.BigIntegerField()
    pu_email          = models.EmailField(max_length=255, null=True, blank=True, unique=True)


    du_ftusha         = models.ImageField(upload_to= profile_upto, null=True, blank=True)
    du_nmusha         = models.CharField(max_length=255)
    du_alusha         = models.TextField(max_length=255)  
    # du_btkusha        = models.PositiveIntegerField(choices=BENTUK_USAHA, default=1)
    # du_bdgusha        = models.PositiveIntegerField(choices=BIDANG_USAHA, default=1)
    du_btkusha        = models.ManyToManyField(BentukUsaha,  blank=True)
    du_bdgusha        = models.ManyToManyField(BidangUsaha,  blank=True)
    du_thnbrdr        = models.BigIntegerField(default=2000)
    du_lat            = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    du_long           = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)


    dtu_tujuan        = models.CharField(max_length=250, null=True, blank=True)
    dtu_omzetthn      = models.BigIntegerField(null=True, blank=True)
    dtu_totalaset      = models.BigIntegerField(null=True, blank=True)
    dtu_skalausha     = models.PositiveIntegerField(choices=SKALA_USAHA, default=1)
    dtu_wktutggu      = models.BigIntegerField(null=True, blank=True,)
    dtu_bypsnunit     = models.BigIntegerField(null=True, blank=True)
    dtu_bysmpunit     = models.BigIntegerField(null=True, blank=True)
    dtu_kltsharga     = models.SmallIntegerField(null=True, blank=True)
    dtu_kltskirim     = models.SmallIntegerField(null=True, blank=True)
    dtu_hrgakirim     = models.SmallIntegerField(null=True, blank=True)
    
    
    dtu_uraimslh      = models.TextField(null=True, blank=True,)  

    created_by      = models.CharField(max_length=25,blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=25,blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.du_nmusha

    class Meta:
        db_table = 'umkm_data'
        verbose_name_plural = 'umkm_data'





class Pendidikan(models.Model):
    judul        = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='judul', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul

    class Meta:
        db_table = 'pendidikan_data'
        verbose_name_plural = 'pendidikan_data'


class JenisTenagaKerja(models.Model):
    judul        = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='judul', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul

    class Meta:
        db_table = 'jenis_tenaga_kerja'
        verbose_name_plural = 'jenis_tenaga_kerja'

    
class TipePerijinan(models.Model):
    judul        = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='judul', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul

    class Meta:
        db_table = 'tipe_perijinan'
        verbose_name_plural = 'tipe_perijinan'

class JenisEnergi(models.Model):
    judul        = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='judul', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul

    class Meta:
        db_table = 'jenis_energi'
        verbose_name_plural = 'jenis_energi'

class TipeFasilitas(models.Model):
    judul        = models.CharField(max_length=200)
    deskripsi    = models.CharField(max_length=200, default="", blank=True) 
    slug         = AutoSlugField(populate_from='judul', editable=True, unique=True, blank=True, null=True)

    def __str__(self):
        return self.judul

    class Meta:
        db_table = 'tipe_fasilitas'
        verbose_name_plural = 'tipe_fasilitas'



class DetailTenagaKerja(models.Model):

    jenis_tngkrj = models.ForeignKey(JenisTenagaKerja, on_delete=models.CASCADE, null = True, blank = True)
    jml_org      = models.IntegerField(null=True, blank=True)
    pendidikan   = models.ForeignKey(Pendidikan, on_delete=models.CASCADE, null = True, blank = True)
    umkmid       = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    def __str__(self):
        return str(self.jenis_tngkrj)

    class Meta:
        db_table = 'detail_tenaga_kerja'
        verbose_name_plural = 'detail_tenaga_kerja'


class DetailPerijinan(models.Model):

    tipe_ijin    = models.ForeignKey(TipePerijinan, on_delete=models.CASCADE, null = True, blank = True)
    no_ijin      = models.IntegerField(null=True, blank=True)
    tgl_ijin     = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    umkmid        = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )
   
    def __str__(self):
        return str(self.tipe_ijin)

    class Meta:
        db_table = 'detail_perijinan'
        verbose_name_plural = 'detail_perijinan'



class DetailBahanBaku(models.Model):

    jen_bhbaku   = models.CharField(max_length=200)
    volume       = models.IntegerField(null=True, blank=True)
    nilai        = models.IntegerField(null=True, blank=True)
    asalBB       = models.CharField(max_length=200, null=True, blank=True)
    umkmid        = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    def __str__(self):
        return self.jen_bhbaku

    class Meta:
        db_table = 'detail_bahan_baku'
        verbose_name_plural = 'detail_bahan_baku'


class DetailEnergi(models.Model):
    
    jen_energi   = models.ForeignKey(JenisEnergi, on_delete=models.CASCADE, null = True, blank = True)
    kapasitas    = models.IntegerField(null=True, blank=True)
    keterangan   = models.CharField(max_length=200, null=True, blank=True)
    umkmid       = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    def __str__(self):
        return str(self.jen_energi)

    class Meta:
        db_table = 'detail_pakai_energi'
        verbose_name_plural = 'detail_pakai_energi'


class DetailMesin(models.Model):
    nm_mesin   = models.CharField(max_length=200, null=True, blank=True)
    desc_mesin   = models.CharField(max_length=250, null=True, blank=True)
    jml_mesin    = models.IntegerField(null=True, blank=True)
    umkmid       = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    def __str__(self):
        return self.nm_mesin

    class Meta:
        db_table = 'detail_alat_mesin'
        verbose_name_plural = 'detail_alat_mesin'


class DetailFasilitas(models.Model):
    tipe_fasi    = models.ForeignKey(TipeFasilitas, on_delete=models.CASCADE, null = True, blank = True) 
    nm_fasi      = models.CharField(max_length=250, null=True, blank=True)
    thn_fasi     = models.IntegerField(null=True, blank=True)
    umkmid       = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    def __str__(self):
        return self.nm_fasi

    class Meta:
        db_table = 'detail_fasilitas'
        verbose_name_plural = 'detail_fasilitas'

class DetailPelatihan(models.Model):
    nm_pelat        = models.CharField(max_length=250, null=True, blank=True)
    tmpt_pelat      = models.CharField(max_length=250, null=True, blank=True)
    thn_pelat       = models.IntegerField(null=True, blank=True)
    umkmid          = models.ForeignKey(UmkmModel, on_delete=models.CASCADE, null = True, blank = True )

    def __str__(self):
        return self.nm_pelat

    class Meta:
        db_table = 'detail_pelatihan'
        verbose_name_plural = 'detail_pelatihan'