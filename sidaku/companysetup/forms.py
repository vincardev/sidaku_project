
from django import forms

from .models import CompanySetupModel, SupportCenterModel
from django.forms.widgets import ClearableFileInput, CheckboxInput

class FormCompSetup(forms.ModelForm):
    
    class Meta:
        model = CompanySetupModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormCompSetup, self).__init__(*args, **kwargs)

        self.fields['compName'].widget     = forms.TextInput({'class': 'form-control','placeholder':''})
        self.fields['compLogo'].widget     = ClearableFileInput ()

        self.fields['compDesc'].widget      = forms.Textarea({'class': 'form-control','placeholder':'Masukan Keterangan'})
        self.fields['compAddr'].widget      = forms.Textarea({'class': 'form-control','placeholder':'Alamat Lengkap Beserta Kode Pos'})
      
        self.fields['compPhone'].widget     = forms.NumberInput({'class': 'form-control', 'type': 'tel','placeholder':'(0341)'})
        self.fields['compEmail'].widget     = forms.EmailInput({'class': 'form-control','placeholder':'@gmail.com'})
        self.fields['compFb'].widget        = forms.TextInput({'class': 'form-control','placeholder':'www.facebook.com/'})
        self.fields['compIg'].widget        = forms.TextInput({'class': 'form-control','placeholder':'www.instagram.com/'})
        self.fields['compWeb'].widget       = forms.TextInput({'class': 'form-control'})

        self.fields['compAdm1'].widget      = forms.NumberInput({'class': 'form-control', 'type': 'tel', 'placeholder': 'wa.me/62'})
        self.fields['compAdm2'].widget      = forms.NumberInput({'class': 'form-control', 'type': 'tel', 'placeholder': 'wa.me/62'})
        self.fields['compAdmNm1'].widget     = forms.TextInput({'class': 'form-control','placeholder':'Nama Lengkap'})
        self.fields['compAdmNm2'].widget     = forms.TextInput({'class': 'form-control','placeholder':'Nama Lengkap'})
        self.fields['compAdmFt1'].widget     = ClearableFileInput ()
        self.fields['compAdmFt2'].widget     = ClearableFileInput ()


        self.fields['partName'].widget     = forms.TextInput({'class': 'form-control'})
        self.fields['partLogo'].widget     = ClearableFileInput ()

        self.fields['partDesc'].widget      = forms.Textarea({'class': 'form-control','placeholder':'Masukan Keterangan'})
        self.fields['partAddr'].widget      = forms.Textarea({'class': 'form-control'})
        
        self.fields['created_by'].widget    = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})
        self.fields['modified_by'].widget   = forms.TextInput({'class': 'form-control', 'hidden': 'hidden'})

        self.fields['created_by'].label     = ""
        self.fields['modified_by'].label    = ""

        self.fields['compLogo'].label       = "Logo PLUT KUMKM Kota Batu"
        self.fields['compName'].label       = "Title Logo PLUT"
        self.fields['compDesc'].label       = "Keterangan PLUT KUMKM Kota Batu"
        self.fields['compAddr'].label       = "Alamat Kantor PLUT KUMKM Kota Batu"

        self.fields['compPhone'].label      = "Telepon"
        self.fields['compEmail'].label      = "Email"
        self.fields['compFb'].label         = "link Facebook"
        self.fields['compIg'].label         = "Link Instagram"
        self.fields['compWeb'].label        = "Website"

        self.fields['compAdm1'].label       = "Link Whatsapp Narahubung 1"
        self.fields['compAdm2'].label       = "Link Whatsapp Narahubung 2"
        self.fields['compAdmNm1'].label     = "Nama Narahubung 1"
        self.fields['compAdmNm2'].label     = "Nama Narahubung 2"
        self.fields['compAdmFt1'].label     = "Foto Narahubung 1"
        self.fields['compAdmFt2'].label     = "Foto Narahubung 2"

        self.fields['partLogo'].label       = "Logo SIDAKU"
        self.fields['partName'].label       = "Title Logo SIDAKU"
        self.fields['partDesc'].label       = "Keterangan SIDAKU"
        self.fields['partAddr'].label       = "Alamat Partner"


class FormSupportCenter(forms.ModelForm):
    
    class Meta:
        model = SupportCenterModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(FormSupportCenter, self).__init__(*args, **kwargs)

        self.fields['scName'].widget     = forms.TextInput({'class': 'form-control','placeholder':'Nama Lengkap'})
        self.fields['scPhone'].widget     = forms.NumberInput({'class': 'form-control', 'type': 'tel','placeholder':'+62'})
        self.fields['scSubjek'].widget     = forms.TextInput({'class': 'form-control','placeholder':'subjek Pesan'})
        self.fields['scEmail'].widget     = forms.EmailInput({'class': 'form-control','placeholder':'@gmail.com'})
        self.fields['scMsgs'].widget      = forms.Textarea({'class': 'form-control','placeholder':'Tuliskan pesan Anda di sini'})

        self.fields['scName'].label        = "Nama Anda"
        self.fields['scPhone'].label       = "Telepon"
        self.fields['scEmail'].label       = "Email"
        self.fields['scSubjek'].label      = "Subjek"
        self.fields['scMsgs'].label        = "Pesan"
