from django.db import models

from django.template.defaultfilters import slugify
# from .models import UserProfile
import os

from userprofile.models import UserProfile

# from .models import ProdukModel



class KoperasiModel(models.Model):

    def profile_upto(self, instance=None):
        if instance:
            return os.path.join("koperasi", "profil",instance)
        return None

    def documents_upto(self, instance=None):
        if instance:
            return os.path.join("koperasi", "documents", instance)
        return None

    KSM     = 1
    SP      = 2
    JS      = 3
    PRD     = 4
    PMS     = 5

    JENIS_KOPERASI = [
        (KSM, ("Konsumen")),
        (SP, ("Simpan Pinjam")),
        (JS, ("Jasa")),
        (PRD, ("Produsen")),
        (PMS, ("Pemasaran"))
    ]


    dt_user           = models.ForeignKey(UserProfile, default=1, on_delete=models.SET_DEFAULT)

    du_ftkop          = models.ImageField(upload_to= profile_upto, null=True, blank=True)
    du_nakop          = models.CharField(max_length=255)
    du_alkop          = models.TextField(max_length=255)  
    du_jenkop         = models.PositiveIntegerField(choices=JENIS_KOPERASI, default=1, null=True, blank=True)
    du_bhkkop         = models.CharField(max_length=150, null=True, blank=True)

    da_nmketua        = models.CharField(max_length=250, null=True, blank=True)
    da_nmsekre        = models.CharField(max_length=250, null=True, blank=True)
    da_nmbenda        = models.CharField(max_length=250, null=True, blank=True)
    da_nmpngla        = models.CharField(max_length=250, null=True, blank=True)
    da_nmpngws        = models.CharField(max_length=250, null=True, blank=True)
    da_jmlaggt        = models.BigIntegerField(null=True, blank=True, default=0)
    da_jmlkrywn       = models.BigIntegerField(null=True, blank=True, default=0)
    da_tglrat         = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    da_jmlhdrrat      = models.BigIntegerField(null=True, blank=True, default=0)

    pj_jassimkop      = models.FileField(upload_to=documents_upto, null=True, blank=True)
    pj_jaspinkop      = models.FileField(upload_to=documents_upto, null=True, blank=True)
    # pj_jenprod        = models.ForeignKey(ProdukModel, on_delete=models.CASCADE, null = True, blank = True )
    pj_produngkop     = models.FileField(upload_to=documents_upto, null=True, blank=True)

    rkp_lat         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    rkp_long        = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    rkp_tglinput    = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    rkp_nmpmlk      = models.CharField(null=True, blank=True,max_length=255)
    rkp_nikpmlk     = models.BigIntegerField(blank=True, null=True)
    rkp_nibkop      = models.BigIntegerField(blank=True, null=True)


    doc_ketuakop     = models.FileField(upload_to=documents_upto, null=True, blank=True)
    doc_sekrekop     = models.FileField(upload_to=documents_upto, null=True, blank=True)
    doc_bendakop     = models.FileField(upload_to=documents_upto, null=True, blank=True)
    doc_pnglakop     = models.FileField(upload_to=documents_upto, null=True, blank=True)
    doc_pngwskop     = models.FileField(upload_to=documents_upto, null=True, blank=True)

    created_by      = models.CharField(max_length=25,blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=25,blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.du_nakop

    class Meta:
        db_table = 'koperasi_data'
        verbose_name_plural = 'koperasi_data'


class KategoriIPModel(models.Model):


    IPKATLIST = [
        ("tata-kelola", ("TATA KELOLA")),
        ("profil-risiko", ("PROFIL RISIKO")),
        ("kinerja", ("KINERJA")),
        ("permodalan", ("PERMODALAN")),
    ]

    IPSUBKATLIST = [
        ("prinsip-koperasi", ("PRINSIP KOPERASI")),
        ("kelembagaan", ("KELEMBAGAAN")),
        ("manajemen", ("MANAJEMEN")),

        ("risiko-operasional", ("Risiko Operasional")),
        ("risiko-kepatuhan", ("Risiko Kepatuhan")),
        ("risiko-likuiditas", ("Risiko Likuiditas")),
        ("kpmr-pinjaman", ("Kualitas Penerapan Manajemen Risiko Pinjaman/pembiayaan")),
        ("kpmr-operasional", ("Kualitas Penerapan Manajemen Risiko Operasional")),
        ("kpmr-kepatuhan", ("Kualitas Penerapan Manajemen Risiko Kepatuhan")),
        ("kpmr-likuiditas", ("Kualitas Penerapan Manajemen Risiko Likuiditas")),

        ("rentabilitas-kemandirian", ("Rentabilitas dan Kemandirian")),
        ("efisiensi", ("Efisiensi")),
        ("kualitas-aset", ("Kualitas Aset")),
        ("aspek-likuiditas", ("Aspek Likuiditas")),

        ("pertumbuhan", ("Pertumbuhan")),
        ("aspek-jatidiri", ("Aspek Jatidiri")),
    ]

    TAGSUBKAT = [
        ("", ("")),
        ("risiko-inheren", ("RISIKO INHEREN ")),
        ("kualitas-manajemen-risiko", ("KUALITAS PENERAPAN MANAJEMEN RISIKO")),
        ("evaluasi-kinerja-keuangan", ("EVALUASI KINERJA KEUANGAN")),
        ("manajemen-keuangan", ("MANAJEMEN KEUANGAN")),
        ("kesinambungan-keuangan", ("KESINAMBUNGAN KEUANGAN")),
        ("kualitas-manajemen-risiko", ("KUALITAS PENERAPAN MANAJEMEN RISIKO")),
        ("kecukupan-modal", ("KECUKUPAN PERMODALAN")),
        ("kecukupan-pengelolaan-modal", ("KECUKUPAN PENGELOLAAN PERMODALAN")),

    ]

    

    ip_var            = models.CharField(max_length=250, null=True, blank=True)
    ipkat             = models.CharField(choices=IPKATLIST, default="tata-kelola", null=True, blank=True, max_length=200)
    ipsubkat          = models.CharField(choices=IPSUBKATLIST, default="prinsip-koperasi", null=True, blank=True, max_length=200)
    tagsubkat          = models.CharField(choices=TAGSUBKAT, default="", null=True, blank=True, max_length=200)


    def __str__(self):
        return self.ip_var

    class Meta:
        db_table = 'kategori_ip'
        verbose_name_plural = 'kategori_ip'

class DPPatuhModel(models.Model):


    kat_var         = models.ForeignKey(KategoriIPModel, default=1, on_delete=models.SET_DEFAULT)
    ind_ukur        = models.CharField(max_length=255, null=True, blank=True)
    dok_pendukung   = models.CharField(max_length=255, null=True, blank=True)
    temuan          = models.CharField(max_length=255, null=True, blank=True)
    
    def __str__(self):
        return self.ind_ukur

    class Meta:
        db_table = 'dp_patuh'
        verbose_name_plural = 'dp_patuh'


class DetailDpPatuh(models.Model):
    choose_dp   = models.ForeignKey(DPPatuhModel, on_delete=models.CASCADE)
    choose_kop  = models.ForeignKey(KoperasiModel, on_delete=models.CASCADE)
    nilai_dp    = models.SmallIntegerField(default=0,blank=True, null=True)

    def __str__(self):
        return str(self.id)