from django import forms
from .models import *

from django.forms.widgets import ClearableFileInput


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

class FormProdukUMKM(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = ProdukUMKM
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormProdukUMKM, self).__init__(*args, **kwargs)  

        self.fields['komoditi'].widget          = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['volume'].widget            = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['satuan'].widget            = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['harga'].widget             = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['total'].widget             = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['fotoprod'].widget          = ClearableFileInput ()


        self.fields['komoditi'].label           = "Komoditi"
        self.fields['volume'].label             = "Volume"
        self.fields['satuan'].label             = "Satuan"
        self.fields['harga'].label              = "Harga"
        self.fields['total'].label              = "Total"
        self.fields['fotoprod'].label           = "Foto Produk"



class FormDemandProdUMKM(forms.ModelForm):
    class Meta:
        model = DetDemandProd
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormDemandProdUMKM, self).__init__(*args, **kwargs)  

        self.fields['dpd_nmprod'].widget          = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['dpd_bulan'].widget           = forms.Select({'class': 'form-select','placeholder':'-- Pilih Bulan --'}, choices=LIST_BULAN)
        self.fields['dpd_tahun'].widget           = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['dpd_demand'].widget          = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['dpd_produksi'].widget        = forms.NumberInput({'class': 'form-control','placeholder':''})
      

        self.fields['dpd_nmprod'].label           = "Nama Produk"
        self.fields['dpd_bulan'].label            = "Bulan"
        self.fields['dpd_tahun'].label            = "Tahun"
        self.fields['dpd_demand'].label           = "Permintaan"
        self.fields['dpd_produksi'].label         = "Produksi"



class FormDemandSuppUMKM(forms.ModelForm):
    class Meta:
        model = DetDemandSup
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormDemandSuppUMKM, self).__init__(*args, **kwargs)  

        self.fields['dsp_jensup'].widget          = forms.Select({'class': 'form-select','placeholder':'-- Pilih Pemasok --'}, choices=LIST_JEN_SUPP)
        self.fields['dsp_bulan'].widget           = forms.Select({'class': 'form-select','placeholder':'-- Pilih Bulan --'}, choices=LIST_BULAN)
        self.fields['dsp_tahun'].widget           = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['dsp_demand'].widget          = forms.NumberInput({'class': 'form-control','placeholder':''})
        self.fields['dsp_produksi'].widget        = forms.NumberInput({'class': 'form-control','placeholder':''})
      
        self.fields['dsp_jensup'].label           = "Jenis Pemasok"
        self.fields['dsp_bulan'].label            = "Bulan"
        self.fields['dsp_tahun'].label            = "Tahun"
        self.fields['dsp_demand'].label           = "Permintaan"
        self.fields['dsp_produksi'].label         = "Produksi"

class FormNilaiSuppUMKM(forms.ModelForm):
    class Meta:
        model = DetPenilaianSupp
        fields = '__all__'
        exclude = ['umkmid']

    def __init__(self, *args, **kwargs):
        super(FormNilaiSuppUMKM, self).__init__(*args, **kwargs)  

        self.fields['dps_nm_supp'].widget        = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['dps_kualitas'].widget       = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['dps_pengiriman'].widget     = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['dps_harga'].widget          = forms.NumberInput({'class': 'form-control','placeholder':''})
      
        self.fields['dps_nm_supp'].label         = "Nama Pemasok"
        self.fields['dps_kualitas'].label        = "Kualitas"
        self.fields['dps_pengiriman'].label      = "Pengiriman"
        self.fields['dps_harga'].label           = "Harga"