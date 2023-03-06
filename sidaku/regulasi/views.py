from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.contrib import messages

from .models import RegulasiModel
from .forms import FormPaparan, FormRapatKoordinasi, FormRegProdHK
from django.core.paginator import Paginator

# Create your views here.

@login_required(login_url=settings.LOGIN_URL)
def master_regul(request):
    search =""
    
    tables_1 = RegulasiModel.objects.filter(type = 1)
    tables_2 = RegulasiModel.objects.filter(type = 2)
    tables_3 = RegulasiModel.objects.filter(type = 3)

    if request.GET:
        search = request.GET.get('search')
        query = (Q(title__icontains=search) | Q(kategori__icontains=search) | 
        Q(tahun__icontains=search)) 
        tables_1 = tables_1.filter(query )
        tables_2 = tables_2.filter(query )
        tables_3 = tables_3.filter(query )
        

    
    paginator_1   = Paginator(tables_1, 10) # Show 25 contacts per page.
    page_number_1 = request.GET.get('page_1')
    page_reg_1    = paginator_1.get_page(page_number_1)

    paginator_2   = Paginator(tables_2, 10) # Show 25 contacts per page.
    page_number_2 = request.GET.get('page_2')
    page_reg_2   = paginator_2.get_page(page_number_2)

    paginator_3   = Paginator(tables_3, 10) # Show 25 contacts per page.
    page_number_3 = request.GET.get('page_3')
    page_reg_3   = paginator_3.get_page(page_number_3)

    tab_active = 'tab_1'
    if page_number_2 :
        tab_active = 'tab_2'
    elif page_number_3 :
        tab_active = 'tab_3'
    elif page_number_1 :
        tab_active = 'tab_1'
    
    
    list_data = {
        'side_active'   : 'regul',
        'tables_1' : tables_1,
        'tables_2' : tables_2,
        'tables_3' : tables_3,
        'page_reg_1' : page_reg_1,
        'page_reg_2' : page_reg_2,
        'page_reg_3' : page_reg_3,
        'tab_active' : tab_active,
    }

    return render (request, 'master_regul.html', list_data)




@login_required(login_url=settings.LOGIN_URL)
def update_regul(request, regul_id):

    tables = RegulasiModel.objects.get(id = regul_id)

    template = 'update_regul.html'
    if request.POST:
        if tables.type == 1:
            form = FormRegProdHK(request.POST, request.FILES, instance = tables)
        elif tables.type == 2:
            form = FormRapatKoordinasi(request.POST, request.FILES, instance = tables)
        else:
            form = FormPaparan(request.POST, request.FILES, instance = tables)

        if form.is_valid():
            post = form.save(commit=False)
            post.modified_by = str(request.user)
            post.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('regul:update_regul', regul_id)
        else:
            messages.error(request, "Data Gagal Di Ubah")

            if tables.type == 1:
                form = FormRegProdHK(instance=tables)
            elif tables.type == 2:
                form = FormRapatKoordinasi(instance=tables)
            else:
                form = FormPaparan(instance=tables)
        
    else:
        if tables.type == 1:
            form = FormRegProdHK(instance=tables)
        elif tables.type == 2:
            form = FormRapatKoordinasi(instance=tables)
        else:
            form = FormPaparan(instance=tables)

    list_data = {
        'side_active'   : 'regul',
        'form'          : form,
        'tables'        : tables
    }
    return render (request, template, list_data)

@login_required(login_url=settings.LOGIN_URL)
def add_regul(request, type_id):
    tables = RegulasiModel.objects.all()

    if request.POST:

        if type_id == 1:
            form = FormRegProdHK(request.POST, request.FILES)
        elif type_id == 2:
            form = FormRapatKoordinasi(request.POST, request.FILES)
        else:
            form = FormPaparan(request.POST, request.FILES)

            
        if form.is_valid():
            post = form.save(commit=False)
            post.type = type_id
            post.save()

            if type_id == 1:
                form = FormRegProdHK()
            elif type_id == 2:
                form = FormRapatKoordinasi()
            else:
                form = FormPaparan()

            messages.success(request, "data berhasil disimpan")
            list_data = {
                'side_active'   : 'regul',
                'form'          : form,
                'tables'        : tables,
                'typeid'        : type_id,
            }

            return redirect('regul:add_regul', type_id)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        if type_id == 1:
            form = FormRegProdHK()
        elif type_id == 2:
            form = FormRapatKoordinasi()
        else:
            form = FormPaparan()

    list_data = {
        'side_active'   : 'regul',
        'form'          : form,
        'tables'        : tables,
        'typeid'         : type_id,
    }

    return render (request, 'add_regul.html', list_data)

@login_required(login_url=settings.LOGIN_URL)
def del_regul(request, regul_id):
    field = RegulasiModel.objects.filter(id = regul_id)
    field.delete()
    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('regul:master_regul')