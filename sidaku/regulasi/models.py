from django.db import models


from django.template.defaultfilters import slugify
import os

class RegulasiModel(models.Model):


    UU     = 1
    PUU    = 2
    PPEM   = 3
    PPRES  = 4
    KIP    = 5
    PMEN   = 6
    KEPMEN = 7
    KEPDEP = 8
    PTER   = 9
    PETPEL = 10
    SUED   = 11

    KATEGORI_CHOICES = [
        (UU, ("Undang-Undang")),
        (PUU, ("Perancangan Undang-Undang")),
        (PPEM, ("Peraturan Pemerintah")),
        (PPRES, ("Peraturan Presiden")),
        (KIP, ("Keputusan dan Intruksi Presiden")),
        (PMEN, ("Peraturan Mentri")),
        (KEPMEN, ("Keputusan Mentri")),
        (KEPDEP, ("Keputusan Deputi")),
        (PTER, ("Peraturan Terkait")),
        (PETPEL, ("Petunjuk Pelaksanaan")),
        (SUED, ("Surat Edaran")),
    ]


    PRODHK      = 1
    RPTKOR      = 2
    PPRN        = 3

    TYPE_CHOICES = [
        (PRODHK, ("Produk Hukum")),
        (RPTKOR, ("Rapat Koordinasi")),
        (PPRN, ("Paparan")),
    ]

    title          = models.CharField(max_length=255)
    type           = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, null=True, blank=True)
    tahun          = models.IntegerField(null=True, blank=True)
    kategori       = models.PositiveIntegerField(choices=KATEGORI_CHOICES, null=True, blank=True)
    documentFile   = models.FileField(upload_to="documents/regulasi/")

    created_by      = models.CharField(max_length=25,blank=True, null=True)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_by     = models.CharField(max_length=25,blank=True, null=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'regulasi_data'
        verbose_name_plural = 'regulasi_data'

    # def __str__(self):
    #     return self.name



    # class Meta:
    #     verbose_name_plural = "Series"
    #     ordering = ['-published']

