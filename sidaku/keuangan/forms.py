from django import forms

from keuangan.models import KeuanganModel
from koperasi.models import KoperasiModel
from django.forms.widgets import ClearableFileInput, CheckboxInput

from keuangan.models import KeuanganUMKMModel
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

class FormKeuangan(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = KeuanganModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormKeuangan, self).__init__(*args, **kwargs)   
        
        koplist = [('0', '---------')] + [ (i.id, i.du_nakop ) for i in KoperasiModel.objects.all() ]

        self.fields['doc_nmkop'].widget          = forms.Select({'class': 'form-select'}, choices =koplist)
        self.fields['doc_bulan'].widget          = forms.Select({'class': 'form-select','placeholder':'-- Pilih Bulan --'}, choices=LIST_BULAN)
        self.fields['doc_tahun'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '2000'})
        self.fields['doc_labrug'].widget         = forms.FileInput({'class': 'form-control'})
        self.fields['doc_neraca'].widget         = forms.FileInput({'class': 'form-control'})
        self.fields['doc_aruskas'].widget        = forms.FileInput({'class': 'form-control'})
        self.fields['doc_permodal'].widget       = forms.FileInput({'class': 'form-control'})
        self.fields['doc_catlapkeu'].widget      = forms.FileInput({'class': 'form-control'})


        self.fields['lps_kas'].widget           = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_bank'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_pinjang'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_pinjcet'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_pendrima'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_bbmuka'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_piutagih'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_aslancar'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_persdbrg'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_persdkon'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_piusha'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_tanah'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_bngn'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_akpbngn'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_invenkntr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_akpinvkntr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_astdklcr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        self.fields['lpk_simpsuk'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_simpberj'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_hutush'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_bbymbyr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_hutlain'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        
        self.fields['lpe_simppkk'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_simpwjb'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_donasi'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_cadresk'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_modpnyt'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        
        self.fields['lpp_pendjas'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpp_pendadm'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpp_pendtko'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpp_pendlain'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        self.fields['lpb_bilanghpp'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimp'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasbank'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimplain'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimpjang'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimpkhus'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypiutang'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byasuran'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byaudit'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypajak'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bykeulain'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byrptpeng'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byrptangg'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byjaladin'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bydiklat'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_honorpeng'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypmbina'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byorglain'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_gjkaryawan'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_tunjangan'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_konsumsi'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bytransdin'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypend'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bykarylain'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byatulis'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bylistrik'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bytelp'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byair'].widget           = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byopslain'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})

        self.fields['created_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget      = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})

       
        
        self.fields['doc_nmkop'].label           = "Nama Koperasi"
        self.fields['doc_bulan'].label           = "Bulan"
        self.fields['doc_tahun'].label           = "Tahun"
        self.fields['doc_labrug'].label          = "Laporan Laba Rugi"
        self.fields['doc_neraca'].label          = "Laporan Neraca"
        self.fields['doc_aruskas'].label         = "Laporan Arus Kas"
        self.fields['doc_permodal'].label        = "Laporan Perubahan Modal"
        self.fields['doc_catlapkeu'].label       = "Catatan Laporan Keuangan"
       
        self.fields['lps_kas'].label           = "Kas"
        self.fields['lps_bank'].label          = "Bank"
        self.fields['lps_pinjang'].label       = "Pinjaman Anggota"
        self.fields['lps_pinjcet'].label       = "Pinjaman Macet"
        self.fields['lps_pendrima'].label      = "Pendapatan ymh Diterima"
        self.fields['lps_bbmuka'].label        = "Beban Dibayar Dimuka"
        self.fields['lps_piutagih'].label      = "Penyshn Piutang tak Tertagih"
        self.fields['lps_aslancar'].label      = "Aset Lancar Lain"
        self.fields['lps_persdbrg'].label      = "Persediaan Barang"
        self.fields['lps_persdkon'].label      = "Persediaan Konsinyasi"
        self.fields['lps_piusha'].label        = "Piutang Usaha"
        self.fields['lps_tanah'].label         = "Tanah"
        self.fields['lps_bngn'].label          = "Bangunan"
        self.fields['lps_akpbngn'].label       = "Ak Peny Bangunan"
        self.fields['lps_invenkntr'].label     = "Inventaris Kantor"
        self.fields['lps_akpinvkntr'].label    = "Ak Peny Inventaris Kantor"
        self.fields['lps_astdklcr'].label      = "Aset Tidak Lancar Lain"

        self.fields['lpk_simpsuk'].label       = "Simpanan Sukarela"
        self.fields['lpk_simpberj'].label      = "Simpanan Berjangka"
        self.fields['lpk_hutush'].label        = "Hutang Usaha"
        self.fields['lpk_bbymbyr'].label       = "Beban ymh Dibayar"
        self.fields['lpk_hutlain'].label       = "Hutang Lain Lain"
        
        self.fields['lpe_simppkk'].label           = "Simpanan Pokok"
        self.fields['lpe_simpwjb'].label           = "Simpanan Wajib"
        self.fields['lpe_donasi'].label            = "Donasi"
        self.fields['lpe_cadresk'].label           = "CAD Tujuan Risiko"
        self.fields['lpe_modpnyt'].label           = "Modal Penyertaan"
        
        self.fields['lpp_pendjas'].label           = "Pendapatan Jasa"
        self.fields['lpp_pendadm'].label           = "Pendapatan Administrasi"
        self.fields['lpp_pendtko'].label           = "Pendapatan Toko"
        self.fields['lpp_pendlain'].label          = "Pendapatan Lainnya"
      
        self.fields['lpb_bilanghpp'].label        = "Biaya Langsung HPP"
        self.fields['lpb_jasimp'].label           = "Jasa Simpanan"
        self.fields['lpb_jasbank'].label          = "Jasa Bank"
        self.fields['lpb_jasimplain'].label       = "Jasa Simpanan Lain Lain"
        self.fields['lpb_jasimpjang'].label       = "Jasa Simpanan Berjangka"
        self.fields['lpb_jasimpkhus'].label       = "Jasa Simpanan Khusus"
        self.fields['lpb_bypiutang'].label        = "Biaya Penyshn Piutang tak Tertagih"
        self.fields['lpb_byasuran'].label         = "Biaya Asuransi"
        self.fields['lpb_byaudit'].label          = "Biaya Audit"
        self.fields['lpb_bypajak'].label          = "Biaya Pajak"
        self.fields['lpb_bykeulain'].label        = "Biaya Keuangan Lain lain"
        self.fields['lpb_byrptpeng'].label        = "Biaya Rapat Pengurus"
        self.fields['lpb_byrptangg'].label        = "Biaya Rapat Anggota"
        self.fields['lpb_byjaladin'].label        = "Biaya Perjalanan Dinas"
        self.fields['lpb_bydiklat'].label         = "Biaya Diklat"
        self.fields['lpb_honorpeng'].label        = "Honorarium Pengurus"
        self.fields['lpb_bypmbina'].label         = "Biaya Pembinaan"
        self.fields['lpb_byorglain'].label        = "Biaya Org Lain-lain"
        self.fields['lpb_gjkaryawan'].label       = "Gaji Karyawan"
        self.fields['lpb_tunjangan'].label        = "Tunjangan"
        self.fields['lpb_konsumsi'].label         = "Konsumsi"
        self.fields['lpb_bytransdin'].label       = "Biaya Transportasi Dinas"
        self.fields['lpb_bypend'].label           = "Biaya Pendidikan"
        self.fields['lpb_bykarylain'].label       = "Biaya Karyawan Lain Lain"
        self.fields['lpb_byatulis'].label         = "Biaya Alat Tulis"
        self.fields['lpb_bylistrik'].label        = "Biaya Listrik"
        self.fields['lpb_bytelp'].label           = "Biaya Telepon"
        self.fields['lpb_byair'].label            = "Biaya Air"
        self.fields['lpb_byopslain'].label        = "Biaya Ops Lain Lain"



        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""




class FormKeuanganUMKM(forms.ModelForm):
    # content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))
    class Meta:
        model = KeuanganUMKMModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormKeuanganUMKM, self).__init__(*args, **kwargs)   
        
        umkmlist = [('0', '---------')] + [ (i.id, i.du_nmusha ) for i in UmkmModel.objects.all() ]

        self.fields['doc_nmumkm'].widget          = forms.Select({'class': 'form-select'}, choices =umkmlist)
        self.fields['doc_bulan'].widget          = forms.Select({'class': 'form-select','placeholder':'-- Pilih Bulan --'}, choices=LIST_BULAN)
        self.fields['doc_tahun'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '2000'})
        self.fields['doc_labrug'].widget         = forms.FileInput({'class': 'form-control'})
        self.fields['doc_neraca'].widget         = forms.FileInput({'class': 'form-control'})
        self.fields['doc_aruskas'].widget        = forms.FileInput({'class': 'form-control'})
        self.fields['doc_permodal'].widget       = forms.FileInput({'class': 'form-control'})
        self.fields['doc_catlapkeu'].widget      = forms.FileInput({'class': 'form-control'})


        self.fields['lps_kas'].widget           = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_bank'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_pinjang'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_pinjcet'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_pendrima'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_bbmuka'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_piutagih'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_aslancar'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_persdbrg'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_persdkon'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_piusha'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_tanah'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_bngn'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_akpbngn'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_invenkntr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_akpinvkntr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lps_astdklcr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        self.fields['lpk_simpsuk'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_simpberj'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_hutush'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_bbymbyr'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpk_hutlain'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        
        self.fields['lpe_simppkk'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_simpwjb'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_donasi'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_cadresk'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpe_modpnyt'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        
        self.fields['lpp_pendjas'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpp_pendadm'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpp_pendtko'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpp_pendlain'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        
        self.fields['lpb_bilanghpp'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimp'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasbank'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimplain'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimpjang'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_jasimpkhus'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypiutang'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byasuran'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byaudit'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypajak'].widget         = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bykeulain'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byrptpeng'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byrptangg'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byjaladin'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bydiklat'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_honorpeng'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypmbina'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byorglain'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_gjkaryawan'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_tunjangan'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_konsumsi'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bytransdin'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bypend'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bykarylain'].widget      = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byatulis'].widget        = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bylistrik'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_bytelp'].widget          = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byair'].widget           = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})
        self.fields['lpb_byopslain'].widget       = forms.NumberInput({'class': 'form-control', 'placeholder': '0'})

        self.fields['created_by'].widget       = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget      = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})

       
        
        self.fields['doc_nmumkm'].label          = "Nama UMKM"
        self.fields['doc_bulan'].label           = "Bulan"
        self.fields['doc_tahun'].label           = "Tahun"
        self.fields['doc_labrug'].label          = "Laporan Laba Rugi"
        self.fields['doc_neraca'].label          = "Laporan Neraca"
        self.fields['doc_aruskas'].label         = "Laporan Arus Kas"
        self.fields['doc_permodal'].label        = "Laporan Perubahan Modal"
        self.fields['doc_catlapkeu'].label       = "Catatan Laporan Keuangan"
       
        self.fields['lps_kas'].label           = "Kas"
        self.fields['lps_bank'].label          = "Bank"
        self.fields['lps_pinjang'].label       = "Pinjaman Anggota"
        self.fields['lps_pinjcet'].label       = "Pinjaman Macet"
        self.fields['lps_pendrima'].label      = "Pendapatan ymh Diterima"
        self.fields['lps_bbmuka'].label        = "Beban Dibayar Dimuka"
        self.fields['lps_piutagih'].label      = "Penyshn Piutang tak Tertagih"
        self.fields['lps_aslancar'].label      = "Aset Lancar Lain"
        self.fields['lps_persdbrg'].label      = "Persediaan Barang"
        self.fields['lps_persdkon'].label      = "Persediaan Konsinyasi"
        self.fields['lps_piusha'].label        = "Piutang Usaha"
        self.fields['lps_tanah'].label         = "Tanah"
        self.fields['lps_bngn'].label          = "Bangunan"
        self.fields['lps_akpbngn'].label       = "Ak Peny Bangunan"
        self.fields['lps_invenkntr'].label     = "Inventaris Kantor"
        self.fields['lps_akpinvkntr'].label    = "Ak Peny Inventaris Kantor"
        self.fields['lps_astdklcr'].label      = "Aset Tidak Lancar Lain"

        self.fields['lpk_simpsuk'].label       = "Simpanan Sukarela"
        self.fields['lpk_simpberj'].label      = "Simpanan Berjangka"
        self.fields['lpk_hutush'].label        = "Hutang Usaha"
        self.fields['lpk_bbymbyr'].label       = "Beban ymh Dibayar"
        self.fields['lpk_hutlain'].label       = "Hutang Lain Lain"
        
        self.fields['lpe_simppkk'].label           = "Simpanan Pokok"
        self.fields['lpe_simpwjb'].label           = "Simpanan Wajib"
        self.fields['lpe_donasi'].label            = "Donasi"
        self.fields['lpe_cadresk'].label           = "CAD Tujuan Risiko"
        self.fields['lpe_modpnyt'].label           = "Modal Penyertaan"
        
        self.fields['lpp_pendjas'].label           = "Pendapatan Jasa"
        self.fields['lpp_pendadm'].label           = "Pendapatan Administrasi"
        self.fields['lpp_pendtko'].label           = "Pendapatan Toko"
        self.fields['lpp_pendlain'].label          = "Pendapatan Lainnya"
      
        self.fields['lpb_bilanghpp'].label        = "Biaya Langsung HPP"
        self.fields['lpb_jasimp'].label           = "Jasa Simpanan"
        self.fields['lpb_jasbank'].label          = "Jasa Bank"
        self.fields['lpb_jasimplain'].label       = "Jasa Simpanan Lain Lain"
        self.fields['lpb_jasimpjang'].label       = "Jasa Simpanan Berjangka"
        self.fields['lpb_jasimpkhus'].label       = "Jasa Simpanan Khusus"
        self.fields['lpb_bypiutang'].label        = "Biaya Penyshn Piutang tak Tertagih"
        self.fields['lpb_byasuran'].label         = "Biaya Asuransi"
        self.fields['lpb_byaudit'].label          = "Biaya Audit"
        self.fields['lpb_bypajak'].label          = "Biaya Pajak"
        self.fields['lpb_bykeulain'].label        = "Biaya Keuangan Lain lain"
        self.fields['lpb_byrptpeng'].label        = "Biaya Rapat Pengurus"
        self.fields['lpb_byrptangg'].label        = "Biaya Rapat Anggota"
        self.fields['lpb_byjaladin'].label        = "Biaya Perjalanan Dinas"
        self.fields['lpb_bydiklat'].label         = "Biaya Diklat"
        self.fields['lpb_honorpeng'].label        = "Honorarium Pengurus"
        self.fields['lpb_bypmbina'].label         = "Biaya Pembinaan"
        self.fields['lpb_byorglain'].label        = "Biaya Org Lain-lain"
        self.fields['lpb_gjkaryawan'].label       = "Gaji Karyawan"
        self.fields['lpb_tunjangan'].label        = "Tunjangan"
        self.fields['lpb_konsumsi'].label         = "Konsumsi"
        self.fields['lpb_bytransdin'].label       = "Biaya Transportasi Dinas"
        self.fields['lpb_bypend'].label           = "Biaya Pendidikan"
        self.fields['lpb_bykarylain'].label       = "Biaya Karyawan Lain Lain"
        self.fields['lpb_byatulis'].label         = "Biaya Alat Tulis"
        self.fields['lpb_bylistrik'].label        = "Biaya Listrik"
        self.fields['lpb_bytelp'].label           = "Biaya Telepon"
        self.fields['lpb_byair'].label            = "Biaya Air"
        self.fields['lpb_byopslain'].label        = "Biaya Ops Lain Lain"



        self.fields['created_by'].label         = ""
        self.fields['modified_by'].label        = ""