from django import forms

from koperasi.models import KoperasiModel
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput, CheckboxInput


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

class FormKoperasi(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = KoperasiModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormKoperasi, self).__init__(*args, **kwargs)   
        
        # serieslist = [('0', '---------')] + [ (i.id, i.title) for i in ArticleSeries.objects.all() ]

        userlist = [('0', '---------')] + [ (i.id, i.user.first_name + " " + i.user.last_name) for i in UserProfile.objects.all() ]

        self.fields['dt_user'].widget           = forms.Select({'class': 'form-select'}, choices =userlist)
        self.fields['du_ftkop'].widget          = ClearableFileInput ()
        self.fields['du_nakop'].widget          = forms.TextInput({'class': 'form-control','placeholder':'Nama Koperasi'})
        self.fields['du_alkop'].widget          = forms.Textarea({'class': 'form-control','placeholder':'Alamat Lengkap Beserta Kode Pos'})
        
        self.fields['du_jenkop'].widget         = forms.Select({'class': 'form-select','placeholder':'-- Pilih Jenis Koperasi --'}, choices=JENIS_KOPERASI)
        self.fields['du_bhkkop'].widget         = forms.TextInput({'class': 'form-control','placeholder':'Badan Hukum Koperasi'})
        
        self.fields['da_nmketua'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['da_nmsekre'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['da_nmbenda'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['da_nmpngla'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['da_nmpngws'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})

        self.fields['da_jmlaggt'].widget        = forms.NumberInput({'class': 'form-control', 'default': 0, 'placeholder': ''})
        self.fields['da_jmlkrywn'].widget       = forms.NumberInput({'class': 'form-control', 'default': 0, 'placeholder': ''})
        self.fields['da_tglrat'].widget         = forms.DateInput({'class': 'form-control','type':'date'},format=('%Y-%m-%d'))
        self.fields['da_jmlhdrrat'].widget      = forms.NumberInput({'class': 'form-control', 'default': 0, 'placeholder': ''})

        self.fields['pj_jassimkop'].widget      = forms.FileInput({'class': 'form-control'})
        self.fields['pj_jaspinkop'].widget      = forms.FileInput({'class': 'form-control'})
        self.fields['pj_produngkop'].widget     = forms.FileInput({'class': 'form-control'})


        self.fields['rkp_lat'].widget           = forms.NumberInput({'class': 'form-control','step': 'any'})
        self.fields['rkp_long'].widget          = forms.NumberInput({'class': 'form-control','step': 'any'})
        self.fields['rkp_tglinput'].widget      = forms.DateInput({'class': 'form-control','type':'date'},format=('%Y-%m-%d'))
        self.fields['rkp_nmpmlk'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['rkp_nikpmlk'].widget       = forms.NumberInput({'class': 'form-control', 'default': 0, 'placeholder': ''})
        self.fields['rkp_nibkop'].widget        = forms.NumberInput({'class': 'form-control', 'default': 0, 'placeholder': ''})

        self.fields['doc_ketuakop'].widget     = forms.FileInput({'class': 'form-control'})
        self.fields['doc_sekrekop'].widget     = forms.FileInput({'class': 'form-control'})
        self.fields['doc_bendakop'].widget     = forms.FileInput({'class': 'form-control'})
        self.fields['doc_pnglakop'].widget     = forms.FileInput({'class': 'form-control'})
        self.fields['doc_pngwskop'].widget     = forms.FileInput({'class': 'form-control'})
        self.fields['created_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget      = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        
        
        self.fields['dt_user'].label           = "Data Penginput"
        
        self.fields['du_ftkop'].label          = "Foto Profil Koperasi"
        self.fields['du_nakop'].label          = "Nama Koperasi"
        self.fields['du_alkop'].label          = "Alamat Koperasi"
        self.fields['du_jenkop'].label         = "Jenis Koperasi"
        self.fields['du_bhkkop'].label         = "Badan Hukum Koperasi"
        
        self.fields['da_nmketua'].label        = "Nama Ketua Koperasi"
        self.fields['da_nmsekre'].label        = "Nama Sekretaris Koperasi"
        self.fields['da_nmbenda'].label        = "Nama Bendahara Koperasi"
        self.fields['da_nmpngla'].label        = "Nama Pengelola Koperasi"
        self.fields['da_nmpngws'].label        = "Nama Pengawas Koperasi"
        self.fields['da_jmlaggt'].label        = "Jumlah Anggota"
        self.fields['da_jmlkrywn'].label       = "Jumlah Karyawan"
        self.fields['da_tglrat'].label         = "Tanggal RAT"
        self.fields['da_jmlhdrrat'].label      = "Jumlah Hadir RAT"
       
        self.fields['pj_jassimkop'].label               = "Jasa Simpanan Koperasi"
        self.fields['pj_jaspinkop'].label               = "Jasa Pinjaman Koperasi"
        self.fields['pj_produngkop'].label              = "Produk Unggulan Koperasi"
        
        self.fields['rkp_lat'].label               = "Latitude"
        self.fields['rkp_long'].label               = "Longitude"
        self.fields['rkp_tglinput'].label          = "Tanggal Penginputan"
        self.fields['rkp_nmpmlk'].label            = "Nama Pemilik"
        self.fields['rkp_nikpmlk'].label           = "NIK Pemilik"
        self.fields['rkp_nibkop'].label            = "NIB Koperasi"

        self.fields['doc_ketuakop'].label               = "Dokumen Ketua Koperasi"
        self.fields['doc_sekrekop'].label               = "Dokumen Sekretaris Koperasi"
        self.fields['doc_bendakop'].label               = "Dokumen Bendahara Koperasi"
        self.fields['doc_pnglakop'].label               = "Dokumen Pengelola Koperasi"
        self.fields['doc_pngwskop'].label               = "Dokumen Pengawas Koperasi"

        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""