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
    du_jenkop         = models.PositiveIntegerField(choices=JENIS_KOPERASI)
    du_bhkkop         = models.CharField(max_length=150, null=True, blank=True)

    da_nmketua        = models.CharField(max_length=250, null=True, blank=True)
    da_nmsekre        = models.CharField(max_length=250, null=True, blank=True)
    da_nmbenda        = models.CharField(max_length=250, null=True, blank=True)
    da_nmpngla        = models.CharField(max_length=250, null=True, blank=True)
    da_nmpngws        = models.CharField(max_length=250, null=True, blank=True)
    da_jmlaggt        = models.IntegerField(null=True, blank=True, default=0)
    da_jmlkrywn       = models.IntegerField(null=True, blank=True, default=0)
    da_tglrat         = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    da_jmlhdrrat      = models.IntegerField(null=True, blank=True, default=0)

    pj_jassimkop      = models.FileField(upload_to=documents_upto, null=True, blank=True)
    pj_jaspinkop      = models.FileField(upload_to=documents_upto, null=True, blank=True)
    # pj_jenprod        = models.ForeignKey(ProdukModel, on_delete=models.CASCADE, null = True, blank = True )
    pj_produngkop     = models.FileField(upload_to=documents_upto, null=True, blank=True)

    rkp_lat         = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    rkp_long        = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
    rkp_tglinput    = models.DateField(null=True, blank=True,auto_now=False, auto_now_add=False)
    rkp_nmpmlk      = models.CharField(null=True, blank=True,max_length=255)
    rkp_nikpmlk     = models.IntegerField(blank=True, null=True)
    rkp_nibkop      = models.IntegerField(blank=True, null=True)


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


