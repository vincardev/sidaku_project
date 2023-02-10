
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    first_name  = forms.CharField(max_length=255)
    last_name   = forms.CharField(max_length=255)
    email       = forms.EmailField(help_text='A valid email address, please.', required=True)
    avatar      = forms.ClearableFileInput ({'class': 'form-control'})

    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ['user']

    def save(self, commit=True):
        user = super(UserProfileForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


def form_validation_error(form):
    msg = ""
    for field in form:
        for error in field.errors:
            msg += "%s: %s \\n" % (field.label if hasattr(field, 'label') else 'Error', error)
    return msg


class UserListForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'

    def save(self, commit=True):
        user = super(UserListForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user




class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    first_name = forms.CharField(required=True)
    username = forms.CharField(min_length=5, required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super(UserRegistrationForm, self).__init__(*args, **kwargs)

        self.fields['first_name'].widget     = forms.TextInput({'class': 'form-control'} )
        self.fields['last_name'].widget      = forms.TextInput({'class': 'form-control'})
        self.fields['email'].widget          = forms.EmailInput({'class': 'form-control'})
        self.fields['username'].widget       = forms.TextInput({'class': 'form-control','min_length':5})
        self.fields['password1'].widget      = forms.PasswordInput({'class': 'form-control'})
        self.fields['password2'].widget      = forms.PasswordInput({'class': 'form-control'})

        self.fields['first_name'].label     = "Nama Depan"
        self.fields['last_name'].label      = "Nama Belakang"
        self.fields['username'].label       = "Username"


    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
