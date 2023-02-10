from django import forms
from .models import Article, ArticleSeries
from django.forms.widgets import ClearableFileInput
from ckeditor_uploader.widgets import CKEditorUploadingWidget

class SeriesCreateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "slug",
            "image",
        ]


    def __init__(self, *args, **kwargs):
        super(SeriesCreateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget     = forms.TextInput({'class': 'form-control'})
        self.fields['subtitle'].widget  = forms.Textarea({'class': 'form-control'})
        self.fields['slug'].widget      = forms.TextInput({'class': 'form-control' })
        self.fields['image'].widget     = ClearableFileInput ({'class': 'form-control'})


        self.fields['title'].label              = "Judul Kategori" 
        self.fields['subtitle'].label           = "Subjudul Kategori" 
        self.fields['image'].label              = "Gambar yang ditampilkan" 

class ArticleCreateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "subtitle",
            "series",
            "content",
            "notes",
            "inheadline",
            "ineducate",
            "ingallery",
            "article_slug",
            "image",
        ]


    def __init__(self, *args, **kwargs):
        super(ArticleCreateForm, self).__init__(*args, **kwargs)

        serieslist = [('0', '---------')] + [ (i.id, i.title) for i in ArticleSeries.objects.all() ]


        self.fields['title'].widget             = forms.TextInput({'class': 'form-control'})
        self.fields['subtitle'].widget          = forms.TextInput({'class': 'form-control'})
        self.fields['article_slug'].widget      = forms.TextInput({'class': 'form-control' })
        self.fields['content'].widget           = CKEditorUploadingWidget()
        self.fields['notes'].widget             = CKEditorUploadingWidget()
        self.fields['series'].widget            = forms.Select({'class': 'form-select'}, choices=serieslist)
        self.fields['image'].widget             = ClearableFileInput ({'class': 'form-control'})
        self.fields['inheadline'].widget        = forms.Select({'class': 'form-select'}, choices=[ (False, 'Tidak Aktif'),(True, 'Aktif')])
        self.fields['ineducate'].widget         = forms.Select({'class': 'form-select'}, choices=[ (False, 'Tidak Aktif'),(True, 'Aktif')])
        self.fields['ingallery'].widget         = forms.Select({'class': 'form-select'}, choices=[ (False, 'Tidak Aktif'),(True, 'Aktif')])

        self.fields['ingallery'].label          = "Aktifkan sebagai Gallery?" 
        self.fields['ineducate'].label          = "Aktifkan sebagai Edukasi?" 
        self.fields['inheadline'].label         = "Aktifkan sebagai Headline?" 
        self.fields['series'].label             = "Kategori Berita" 
        self.fields['title'].label              = "Judul Berita" 
        self.fields['subtitle'].label           = "Sub Judul" 
        self.fields['content'].label            = "Isi Berita" 
        self.fields['image'].label              = "Gambar yang ditampilkan" 
        self.fields['article_slug'].label       = "Slug" 

class SeriesUpdateForm(forms.ModelForm):
    class Meta:
        model = ArticleSeries

        fields = [
            "title",
            "subtitle",
            "slug",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super(SeriesUpdateForm, self).__init__(*args, **kwargs)

        self.fields['title'].widget     = forms.TextInput({'class': 'form-control'})
        self.fields['subtitle'].widget  = forms.Textarea({'class': 'form-control'})
        self.fields['slug'].widget      = forms.TextInput({'class': 'form-control' })
        self.fields['image'].widget     = ClearableFileInput ({'class': 'form-control'})

        self.fields['title'].label              = "Judul Kategori" 
        self.fields['subtitle'].label           = "Sub Judul " 
        self.fields['image'].label              = "Gambar yang ditampilkan" 

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article

        fields = [
            "title",
            "subtitle",
            "series",
            "content",
            "notes",
            "inheadline",
            "ineducate",
            "ingallery",
            "article_slug",
            "image",
        ]

    def __init__(self, *args, **kwargs):
        super(ArticleUpdateForm, self).__init__(*args, **kwargs)


        serieslist = [('0', '---------')] + [ (i.id, i.title) for i in ArticleSeries.objects.all() ]

        self.fields['title'].widget             = forms.TextInput({'class': 'form-control'})
        self.fields['subtitle'].widget          = forms.TextInput({'class': 'form-control'})
        self.fields['article_slug'].widget      = forms.TextInput({'class': 'form-control' })
        self.fields['content'].widget           = CKEditorUploadingWidget()
        self.fields['notes'].widget             = CKEditorUploadingWidget()
        self.fields['series'].widget            = forms.Select({'class': 'form-select'}, choices= serieslist)
        self.fields['image'].widget             = ClearableFileInput ({'class': 'form-control'})
        self.fields['inheadline'].widget        = forms.Select({'class': 'form-select'}, choices=[ (False, 'Tidak Aktif'),(True, 'Aktif')])
        self.fields['ineducate'].widget         = forms.Select({'class': 'form-select'}, choices=[ (False, 'Tidak Aktif'),(True, 'Aktif')])
        self.fields['ingallery'].widget         = forms.Select({'class': 'form-select'}, choices=[ (False, 'Tidak Aktif'),(True, 'Aktif')])

        self.fields['ingallery'].label          = "Aktifkan sebagai Gallery?" 
        self.fields['ineducate'].label          = "Aktifkan sebagai Edukasi?" 
        self.fields['inheadline'].label         = "Aktifkan sebagai Headline?" 
        self.fields['series'].label             = "Kategori Berita" 
        self.fields['title'].label              = "Judul Berita" 
        self.fields['subtitle'].label           = "Sub Judul " 
        self.fields['content'].label            = "Isi Berita" 
        self.fields['image'].label              = "Gambar yang ditampilkan" 
        self.fields['article_slug'].label       = "Slug" 