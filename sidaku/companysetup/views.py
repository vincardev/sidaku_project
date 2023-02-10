from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

from .forms import FormCompSetup
from .models import CompanySetupModel
from django.contrib.auth.decorators import login_required
from django.conf import settings

def index(request):
    
    context = {
        "header_menu":"",
        "footer_menu":"",
    }
    return render(request, 'site/add_comp.html', context)


@login_required(login_url=settings.LOGIN_URL)
def add_compsetup(request):

    tables = CompanySetupModel.objects.all()
    if (tables.count() != 0):
        return redirect('setting:updsetting', tables[0].id)

    if request.POST:
        form = FormCompSetup(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = str(request.user)
            post.save()
            form = FormCompSetup()

            messages.success(request, "data berhasil disimpan")
            list_data = {

                'side_active'   : 'compset',
                'form'          : form,
                'tables'        : tables
            }

            return redirect('setting:updsetting', post.pk)
            # return render(request, "site/add_comp.html", list_data)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = FormCompSetup()

    list_data = {

        'side_active'   : 'compset',
        'form'          : form,
        'tables'        : tables,
    }

    return render (request, 'site/add_comp.html', list_data)


@login_required(login_url=settings.LOGIN_URL)
def upd_compsetup(request, comp_id):

    tables = CompanySetupModel.objects.get(id = comp_id)
    template = 'site/upd_comp.html'
    if request.POST:
        form = FormCompSetup(request.POST, request.FILES, instance = tables)
        if form.is_valid():
            post = form.save(commit=False)
            post.modified_by = str(request.user)
            post.save()
            # form.save()
            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('setting:updsetting', comp_id)
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = FormCompSetup(instance=tables)
        
    else:
        form = FormCompSetup(instance=tables)

    list_data = {
        'side_active'   : 'compset',
        'form'          : form,
        'tables'        : tables,
    }
    return render (request, template, list_data)