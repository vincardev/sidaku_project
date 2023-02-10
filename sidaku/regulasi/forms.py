from django import forms

from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from ckeditor.widgets import CKEditorWidget
from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from backend.wilayah_indonesia.models import *

from string import Template
from django.utils.safestring import mark_safe
from django.forms import ImageField
from tinymce.widgets import TinyMCE

from regulasi.models import RegulasiModel


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


class FormRegProdHK(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = RegulasiModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormRegProdHK, self).__init__(*args, **kwargs)     

        self.fields['type'].widget              = forms.TextInput({'class': 'form-control', 'hidden': 'hidden','type':'number','value':1})
        self.fields['title'].widget             = forms.TextInput({'class': 'form-control'})
        self.fields['tahun'].widget             = forms.TextInput({'class': 'form-control','type':'number'})
        self.fields['kategori'].widget          = forms.Select({'class': 'form-select'}, choices =KATEGORI_CHOICES)
        self.fields['documentFile'].widget      = forms.FileInput({'class': 'form-control'})
        self.fields['created_by'].widget        = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        
        self.fields['type'].label               = ""
        self.fields['title'].label              = "Nama Produk Hukum"
        self.fields['tahun'].label              = "Tahun"
        self.fields['kategori'].label           = "Kategori"
        self.fields['documentFile'].label       = "Dokumen Produk Hukum"
        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""


class FormRapatKoordinasi(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = RegulasiModel
        fields = '__all__'
        exclude =['tahun']

    def __init__(self, *args, **kwargs):
        super(FormRapatKoordinasi, self).__init__(*args, **kwargs)     

        self.fields['type'].widget              = forms.TextInput({'class': 'form-control', 'hidden': 'hidden','type':'number','value':2})
        self.fields['title'].widget             = forms.TextInput({'class': 'form-control'})
        # self.fields['tahun'].widget             = forms.TextInput({'class': 'form-control','type':'number'})
        self.fields['kategori'].widget          = forms.Select({'class': 'form-select'}, choices =KATEGORI_CHOICES)
        self.fields['documentFile'].widget      = forms.FileInput({'class': 'form-control'})
        self.fields['created_by'].widget        = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        
        self.fields['type'].label               = ""
        self.fields['title'].label              = "Nama Rapat Koordinasi"
        # self.fields['tahun'].label              = ""
        self.fields['kategori'].label           = "Kategori"
        self.fields['documentFile'].label       = "Dokumen Rapat Koordinasi"
        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""

class FormPaparan(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = RegulasiModel
        fields = '__all__'
        exclude =['tahun','kategori']

    def __init__(self, *args, **kwargs):
        super(FormPaparan, self).__init__(*args, **kwargs)     

        self.fields['type'].widget              = forms.TextInput({'class': 'form-control', 'hidden': 'hidden','type':'number','value':3})
        self.fields['title'].widget             = forms.TextInput({'class': 'form-control'})
        # self.fields['tahun'].widget             = forms.TextInput({'class': 'form-control','type':'number'})
        # self.fields['kategori'].widget          = forms.Select({'class': 'form-select'}, choices =KATEGORI_CHOICES)
        self.fields['documentFile'].widget      = forms.FileInput({'class': 'form-select'})
        self.fields['created_by'].widget        = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        
        self.fields['type'].label               = ""
        self.fields['title'].label              = "Nama Paparan"
        # self.fields['tahun'].label              = ""
        # self.fields['kategori'].label           = ""
        self.fields['documentFile'].label       = "Dokumen Paparan"
        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""
