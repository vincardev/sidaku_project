"""sidaku URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

from sidaku import settings



urlpatterns = [
    path('', include('homepage.urls', namespace='home')),
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    path('sidaku_admin/site_setting/', include('companysetup.urls', namespace='setting')),
    path('sidaku_admin/users/', include("userprofile.urls", namespace='userprofile')),

    path ('sidaku_admin/news/', include('articles.urls', namespace='artic')),
    path ('sidaku_admin/regulasi/', include('regulasi.urls', namespace='regul')),
    path ('sidaku_admin/koperasi/', include('koperasi.urls', namespace='koper')),
    path ('sidaku_admin/umkm/', include('umkmdata.urls', namespace='umkmdat')),
    path ('sidaku_admin/keuangan/', include('keuangan.urls', namespace='uang')),
    path ('sidaku_admin/', include('dashboard.urls', namespace='dash')),
    path ('sidaku_admin/login/', LoginView.as_view(), name='logadmin'),
    path ('signout/', LogoutView.as_view(next_page='logadmin'), name='signout'),

    path('ckeditor/', include('ckeditor_uploader.urls')),

    # path('site_setting/add', include('sitesetup.urls', namespace="sitesetup" )
    # path('site_settings/', include('sitesetup.urls', namespace='setup')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns += staticfiles_urlpatterns()
# // uploadfiles\
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

