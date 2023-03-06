from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *
from django.core.paginator import Paginator

@login_required(login_url=settings.LOGIN_URL)
def master_keu(request):
    search =""
    
    tables = KeuanganModel.objects.all()
    tables_umkm = KeuanganUMKMModel.objects.all()

    # if request.GET:
    #     search = request.GET.get('search')
    #     query = (Q(doc_nmkop__icontains=search) | Q(doc_tahun__icontains=search) | 
    #     Q(doc_bulan__icontains=search)) 
    #     tables = tables.filter(query )
    


    paginator   = Paginator(tables, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page_1')
    page_kop    = paginator.get_page(page_number)

    paginator_2   = Paginator(tables_umkm, 10) # Show 25 contacts per page.
    page_number_2 = request.GET.get('page_2')
    page_umkm    = paginator_2.get_page(page_number_2)

    tab_active = 'tab_kop'
    if page_number_2 :
        tab_active = 'tab_umkm'
    elif page_number :
        tab_active = 'tab_kop'

    list_data = {
        'side_active'   : 'lapkeu',
        'tables' : tables,
        'page_kop' : page_kop,
        'tables_umkm' : tables_umkm,
        'page_umkm' : page_umkm,
        'tab_active' : tab_active,
    }

    return render (request, 'master_keu.html', list_data)


@login_required(login_url=settings.LOGIN_URL)
def add_keu(request):

    tables = KeuanganModel.objects.all()

    if request.POST:
        form = FormKeuangan(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = str(request.user)
            post.save()
            form = FormKeuangan()

            messages.success(request, "data berhasil disimpan")
            list_data = {
                'side_active'   : 'lapkeu',
                'form'          : form,
                'tables'        : tables
            }

            return render(request, "add_keu.html", list_data)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = FormKeuangan()

    list_data = {

        'side_active'   : 'lapkeu',
        'form'          : form,
        'tables'        : tables,
    }

    return render (request, 'add_keu.html', list_data)




@login_required(login_url=settings.LOGIN_URL)
def upd_keu(request, keu_id):

    tables      = KeuanganModel.objects.get(id = keu_id)

    template = 'upd_keu.html'
    if request.POST:
        form = FormKeuangan(request.POST, request.FILES, instance = tables)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_by = str(request.user)
            post.save()

            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('uang:upd_keu', keu_id)
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = FormKeuangan(instance=tables)
        
    else:
        form = FormKeuangan(instance=tables)

    list_data = {
        'side_active'   : 'lapkeu',
        'form'          : form,
        'tables'        : tables,
    }
    return render (request, template, list_data)



@login_required(login_url=settings.LOGIN_URL)
def del_keu(request, keu_id):
    field = KeuanganModel.objects.filter(id = keu_id)
    field.delete()

    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('uang:master_keu')



@login_required(login_url=settings.LOGIN_URL)
def add_keu_umkm(request):

    tables = KeuanganUMKMModel.objects.all()

    if request.POST:
        form = FormKeuanganUMKM(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = str(request.user)
            post.save()
            form = FormKeuanganUMKM()

            messages.success(request, "data berhasil disimpan")
            list_data = {
                'side_active'   : 'lapkeu',
                'form'          : form,
                'tables'        : tables
            }

            return render(request, "add_keu_umkm.html", list_data)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = FormKeuanganUMKM()

    list_data = {

        'side_active'   : 'lapkeu',
        'form'          : form,
        'tables'        : tables,
    }

    return render (request, 'add_keu_umkm.html', list_data)


@login_required(login_url=settings.LOGIN_URL)
def upd_keu_umkm(request, keu_id):

    tables      = KeuanganUMKMModel.objects.get(id = keu_id)

    template = 'upd_keu_umkm.html'
    if request.POST:
        form = FormKeuanganUMKM(request.POST, request.FILES, instance = tables)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_by = str(request.user)
            post.save()

            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('uang:upd_keu_umkm', keu_id)
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = FormKeuanganUMKM(instance=tables)
        
    else:
        form = FormKeuanganUMKM(instance=tables)

    list_data = {
        'side_active'   : 'lapkeu',
        'form'          : form,
        'tables'        : tables,
    }
    return render (request, template, list_data)



@login_required(login_url=settings.LOGIN_URL)
def del_keu_umkm(request, keu_id):
    field = KeuanganUMKMModel.objects.filter(id = keu_id)
    field.delete()

    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('uang:master_keu')

