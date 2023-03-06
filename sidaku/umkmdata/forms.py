from django import forms

from umkmdata.models import *
from userprofile.models import UserProfile
from django.contrib.auth.models import User
from django.forms.widgets import ClearableFileInput, CheckboxInput

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

PERBANDINGAN = [
    (1, ''),
    (2, ''),
    (3, ''),
    (4, ''),
    (5, ''),
    (6, ''),
    (7, ''),
    (8, ''),
    (9, ''),
    ]

class FormUMKM(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = UmkmModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormUMKM, self).__init__(*args, **kwargs)   

        biduslist = [[x.id, x.nama] for x in BidangUsaha.objects.all()]
        bentuslist = [[x.id, x.nama] for x in BentukUsaha.objects.all()]
        
        userlist = [('0', '---------')] + [ (i.id, i.user.first_name + " " + i.user.last_name) for i in UserProfile.objects.all() ]

        self.fields['dt_user'].widget           = forms.Select({'class': 'form-select'}, choices =userlist)
       

        self.fields['pu_noaggta'].widget        = forms.TextInput({'class': 'form-control','placeholder':'Nomor Anggota'})
        self.fields['pu_nmpmlk'].widget         = forms.TextInput({'class': 'form-control','placeholder':'Nama Lengkap Pemilik'})
        self.fields['pu_aldmisi'].widget        = forms.Textarea({'class': 'form-control','placeholder':'Alamat Lengkap Beserta Kode Pos'})
        self.fields['pu_noktp'].widget          = forms.NumberInput({'class': 'form-control','minlength':12, 'placeholder': '16 Digit/ 12 Digit'})
        self.fields['pu_notlp'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '62'})
        self.fields['pu_email'].widget          = forms.EmailInput({'class': 'form-control','placeholder':'@gmail.com'})
    

        self.fields['du_ftusha'].widget          = ClearableFileInput ()
        self.fields['du_nmusha'].widget          = forms.TextInput({'class': 'form-control','placeholder':'Nama Usaha'})
        self.fields['du_alusha'].widget          = forms.Textarea({'class': 'form-control','placeholder':'Alamat Lengkap Beserta Kode Pos'})
        self.fields['du_btkusha'].widget         = forms.CheckboxSelectMultiple({'placeholder':'-- Pilih Bentuk Usaha --'}, choices=bentuslist)
        self.fields['du_bdgusha'].widget         = forms.CheckboxSelectMultiple({'placeholder':'-- Pilih Bidang Usaha --'}, choices=biduslist)
        self.fields['du_thnbrdr'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '2000' ,'maxlength':"4"})
        self.fields['du_lat'].widget             = forms.NumberInput({'class': 'form-control','step': 'any', 'placeholder':'Latitude', 'id':'id_rkp_lat'})
        self.fields['du_long'].widget            = forms.NumberInput({'class': 'form-control','step': 'any', 'placeholder':'Longitude', 'id':'id_rkp_long'})
        
        
        self.fields['dtu_tujuan'].widget         = forms.TextInput({'class': 'form-control','placeholder':'Tujuan/Wilayah Pemasaran'})
        self.fields['dtu_omzetthn'].widget       = forms.NumberInput({'class': 'form-control',  'placeholder': '0'})
        self.fields['dtu_totalaset'].widget       = forms.NumberInput({'class': 'form-control',  'placeholder': '0'})
        self.fields['dtu_skalausha'].widget      = forms.Select({'class': 'form-select','placeholder':'-- Pilih Skala Usaha --'}, choices=SKALA_USAHA)
        self.fields['dtu_wktutggu'].widget       = forms.NumberInput({'class': 'form-control',  'placeholder': '0'})
        self.fields['dtu_bypsnunit'].widget     = forms.NumberInput({'class': 'form-control',  'placeholder': '0'})
        self.fields['dtu_bysmpunit'].widget       = forms.NumberInput({'class': 'form-control',  'placeholder': '0'})
        self.fields['dtu_kltsharga'].widget       = forms.NumberInput({'class': 'form-control',  'hidden': 'hidden'})
        self.fields['dtu_kltskirim'].widget       = forms.NumberInput({'class': 'form-control',  'hidden': 'hidden'})
        self.fields['dtu_hrgakirim'].widget       = forms.NumberInput({'class': 'form-control',  'hidden': 'hidden'})
        self.fields['dtu_uraimslh'].widget        = forms.Textarea({'class': 'form-control','placeholder':'Tuliskan kendala usaha yang dihadapi di sini'})
        
        self.fields['created_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget      = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        
        
        self.fields['dt_user'].label           = "Data Penginput"
        
        self.fields['pu_noaggta'].label        = "Nomor Anggota"
        self.fields['pu_nmpmlk'].label         = "Nama Pemilik"
        self.fields['pu_aldmisi'].label        = "Alamat Domisili"
        self.fields['pu_noktp'].label          = "Nomor KTP/SIM"
        self.fields['pu_notlp'].label          = "Telepon"
        self.fields['pu_email'].label          = "Email"
       
        self.fields['du_ftusha'].label         = "Foto Profil Usaha"
        self.fields['du_nmusha'].label         = "Nama Usaha"
        self.fields['du_alusha'].label         = "Alamat Usaha"
        self.fields['du_btkusha'].label        = "Bentuk Usaha"
        self.fields['du_bdgusha'].label        = "Bidang Usaha"
        self.fields['du_thnbrdr'].label        = "Tahun Berdiri"
        self.fields['du_lat'].label            = "Latitude"
        self.fields['du_long'].label           = "Longitude"
        
        self.fields['dtu_tujuan'].label         = "Wilayah Pemasaran"
        self.fields['dtu_omzetthn'].label       = "Omzet per tahun (Rupiah)"
        self.fields['dtu_totalaset'].label      = "Total Aset (Rupiah)"
        self.fields['dtu_skalausha'].label      = "Skala Usaha"
        self.fields['dtu_wktutggu'].label       = "Waktu Tunggu"
        self.fields['dtu_bypsnunit'].label      = "Biaya Pemesanan per Unit"
        self.fields['dtu_bysmpunit'].label      = "Biaya Penyimpanan per Unit"
        self.fields['dtu_kltsharga'].label      = "Perbandingan Kualitas dan Harga"
        self.fields['dtu_kltskirim'].label      = "Perbandingan Kualitas dan Pengiriman"
        self.fields['dtu_hrgakirim'].label      = "Perbandingan Harga dan Pengiriman"
        self.fields['dtu_uraimslh'].label       = "Uraian Masalah/Kendala"

        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""



class FormTenagaKerjaUMKM(forms.ModelForm):
    class Meta:
        model = DetailTenagaKerja
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormTenagaKerjaUMKM, self).__init__(*args, **kwargs)  

        pendlist = [('0', '---------')] + [ (i.id, i.judul ) for i in Pendidikan.objects.all() ]
        tgkjlist = [('0', '---------')] + [ (i.id, i.judul ) for i in JenisTenagaKerja.objects.all() ]

        self.fields['jenis_tngkrj'].widget      = forms.Select({'class': 'form-select','placeholder':''}, choices=tgkjlist)
        self.fields['jml_org'].widget           = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['pendidikan'].widget        = forms.Select({'class': 'form-select','placeholder':''}, choices=pendlist)
      
        self.fields['jenis_tngkrj'].label       = "Tenaga Kerja"
        self.fields['jml_org'].label            = "Jumlah Orang"
        self.fields['pendidikan'].label         = "Pendidikan"
    


class FormPerijinanUMKM(forms.ModelForm):
    class Meta:
        model = DetailPerijinan
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormPerijinanUMKM, self).__init__(*args, **kwargs)  

        ijinlist = [('0', '---------')] + [ (i.id, i.judul ) for i in TipePerijinan.objects.all() ]

        self.fields['tipe_ijin'].widget      = forms.Select({'class': 'form-select','placeholder':''}, choices=ijinlist)
        self.fields['no_ijin'].widget        = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['tgl_ijin'].widget       = forms.DateInput({'class': 'form-control','type':'date'},format=('%Y-%m-%d'))
      
        self.fields['tipe_ijin'].label       = "Tipe Perijinan"
        self.fields['no_ijin'].label         = "Nomor Perijinan"
        self.fields['tgl_ijin'].label        = "Tanggal Perijinan"



class FormSumEnergiUMKM(forms.ModelForm):
    class Meta:
        model = DetailEnergi
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormSumEnergiUMKM, self).__init__(*args, **kwargs)  

        energilist = [('0', '---------')] + [ (i.id, i.judul ) for i in JenisEnergi.objects.all() ]

        self.fields['jen_energi'].widget      = forms.Select({'class': 'form-select','placeholder':''}, choices=energilist)
        self.fields['kapasitas'].widget        = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['keterangan'].widget       = forms.TextInput({'class': 'form-control','placeholder':''})
      
        self.fields['jen_energi'].label       = "Jenis & Sumber Energi"
        self.fields['kapasitas'].label         = "Kapasitas"
        self.fields['keterangan'].label        = "Keterangan"

class FormBahanBakuUMKM(forms.ModelForm):
    class Meta:
        model = DetailBahanBaku
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormBahanBakuUMKM, self).__init__(*args, **kwargs)  

        self.fields['jen_bhbaku'].widget   = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['volume'].widget       = forms.NumberInput({'class': 'form-control','placeholder':'', 'id':'id_volumebb'})
        self.fields['nilai'].widget        = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['asalBB'].widget       = forms.TextInput({'class': 'form-control','placeholder':''})
      
        self.fields['jen_bhbaku'].label   = "Jenis Bahan Baku/Penolong"
        self.fields['volume'].label       = "Volume"
        self.fields['nilai'].label        = "Nilai"
        self.fields['asalBB'].label       = "Asal BB/BP"


        
class FormDetailMesinUMKM(forms.ModelForm):
    class Meta:
        model = DetailMesin
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormDetailMesinUMKM, self).__init__(*args, **kwargs)  

        self.fields['nm_mesin'].widget   = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['desc_mesin'].widget = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['jml_mesin'].widget  = forms.NumberInput({'class': 'form-control','placeholder':''})
      
        self.fields['nm_mesin'].label   = "Nama Mesin"
        self.fields['desc_mesin'].label = "Keterangan"
        self.fields['jml_mesin'].label  = "Jumlah Mesin"


        

class FormDetailFasilitasUMKM(forms.ModelForm):
    class Meta:
        model = DetailFasilitas
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormDetailFasilitasUMKM, self).__init__(*args, **kwargs)  

        faslist = [('0', '---------')] + [ (i.id, i.judul ) for i in TipeFasilitas.objects.all() ]

        self.fields['tipe_fasi'].widget      = forms.Select({'class': 'form-select','placeholder':''}, choices=faslist)
        self.fields['nm_fasi'].widget       = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['thn_fasi'].widget        = forms.NumberInput({'class': 'form-control','placeholder':''})
      
        self.fields['tipe_fasi'].label       = "Tipe Fasilitas"
        self.fields['nm_fasi'].label         = "Nama Fasilitas"
        self.fields['thn_fasi'].label        = "Tahun Fasilitas"

class FormDetailPelatihanUMKM(forms.ModelForm):
    class Meta:
        model = DetailPelatihan
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormDetailPelatihanUMKM, self).__init__(*args, **kwargs)  

        self.fields['nm_pelat'].widget       = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['tmpt_pelat'].widget     = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['thn_pelat'].widget      = forms.NumberInput({'class': 'form-control','placeholder':''})
      
        self.fields['nm_pelat'].label         = "Nama Pelatihan"
        self.fields['tmpt_pelat'].label       = "Tempat Pelatihan"
        self.fields['thn_pelat'].label        = "Tahun Pelatihan"
