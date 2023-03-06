from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.contrib import messages

from koperasi.models import KoperasiModel
from koperasi.forms import FormKoperasi
from django.http import JsonResponse
from django.db import transaction

from django.core.exceptions import ValidationError
import json

from produk.models import ProdukModel
from koperasi.models import DPPatuhModel, DetailDpPatuh
from keuangan.models import KeuanganModel
from keuangan.forms import *

from .resources import *
from django.http import HttpResponse
from tablib import Dataset
from django.core.paginator import Paginator

@login_required(login_url=settings.LOGIN_URL)
def master_kop(request):
    search =""
    
    tables_1 = KoperasiModel.objects.all()

    if request.GET:
        search = request.GET.get('search')
        query = (Q(du_nakop__icontains=search) | Q(du_alkop__icontains=search) | 
        Q(da_nmketua__icontains=search)  | Q(da_nmpngla__icontains=search) ) 
        tables_1 = tables_1.filter(query)

    if request.POST:
        # Get selected option from form
        file_format = request.POST['file-format']
        post_type = request.POST['post-type']

        if post_type == 'Export':
            koperasi_resource = KoperasiResource()
            dataset = koperasi_resource.export()
            if file_format == 'CSV':
                response = HttpResponse(dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="koperasi_data.csv"'
                return response        
            elif file_format == 'JSON':
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="koperasi_data.json"'
                return response
            elif file_format == 'XLS (Excel)':
                response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="koperasi_data.xlsx"'
                return response   
        
        if post_type == 'Import':
            koperasi_resource = KoperasiResource()
            dataset = Dataset()
            new_koperasi = request.FILES['importData']

            if file_format == 'XLS (Excel)':
                imported_data = dataset.load(new_koperasi.read(),format='xlsx')
                result = koperasi_resource.import_data(dataset, dry_run=True, raise_errors=True)                                                                 
            elif file_format == 'CSV':
                imported_data = dataset.load(new_koperasi.read().decode('utf-8'),format='csv')
                result = koperasi_resource.import_data(dataset, dry_run=True, raise_errors=True)                                                                 
            elif file_format == 'JSON':
                imported_data = dataset.load(new_koperasi.read().decode('utf-8'),format='json')
                # Testing data import
                result = koperasi_resource.import_data(dataset, dry_run=True, raise_errors=True) 

            if not result.has_errors():
                # Import now
                koperasi_resource.import_data(dataset, dry_run=False)

    

    paginator   = Paginator(tables_1, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    list_data = {
        'side_active'   : 'koper',
        'tables_1'      : tables_1,
        'page_obj'      : page_obj,
        'search'        : search,
    }

    return render (request, 'master_kop.html', list_data)

@login_required(login_url=settings.LOGIN_URL)
def add_kop(request):

    tables = KoperasiModel.objects.all()
    # if (tables.count() != 0):
    #     return redirect('setting:updsetting', tables[0].id)
    isFoundError = False
    idprimarykey =''
    if request.POST:
        form = FormKoperasi(request.POST, request.FILES)
        if form.is_valid():
             with transaction.atomic():
                sid = transaction.savepoint()
                try:
                    post = form.save(commit=False)
                    post.created_by = str(request.user)
                    jsonstring = request.POST['jenprod']
                    post.save()
                    idprimarykey = post.pk

                    kopidinstance = KoperasiModel.objects.get(id =post.pk )


                    if jsonstring:
                        json_object = json.loads(jsonstring)

                        if len(json_object)== 0  :
                            isFoundError = True
                            messages.error(request, "Produk Tidak Boleh Kosong" )
                        else:
                            instance_transactions = [
                                ProdukModel(
                                    komoditi = request.POST.get('komoditi-'+ str(idx)),
                                    satuan = request.POST.get('satuan-'+ str(idx)),
                                    volume = request.POST.get('volume-'+ str(idx)),
                                    harga = request.POST.get('harga-'+ str(idx)),
                                    total = request.POST.get('total-'+ str(idx)),
                                    fotoprod = request.FILES.get('fotoprod-'+str(idx)),
                                    kopid=kopidinstance,
                                )
                                for idx, jsondata in enumerate(json_object)
                                #     komoditi=jsondata['komoditi'],
                                #     satuan=jsondata['satuan'],
                                #     volume=jsondata['volume'],
                                #     harga=jsondata['harga'],
                                #     total=jsondata['total'],
                                #     fotoprod=jsondata['foto'],
                                #     kopid=kopidinstance,
                                # )
                                # for jsondata in json_object
                            ]

                            try:
                                ProdukModel.objects.bulk_create(instance_transactions)
                            except Exception as e:
                                messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Inputan Produk")
                                isFoundError = True
                                pass
                            
                    else :
                        isFoundError = True
                        messages.error(request, "Produk Tidak Boleh Kosong" )

                    if isFoundError==False:  
                        form = FormKoperasi()

                        messages.success(request, "data berhasil disimpan")
                        # messages.success(request,  test)
                        list_data = {
                            'side_active'   : 'koper',
                            'form'          : form,
                            'tables'        : tables
                        }

                        # return redirect('koper:add_kop', post.pk)
                        return redirect('koper:upd_kop', idprimarykey)
                        # return render(request, "add_kop.html", list_data)

                except  Exception as e:
                    isFoundError = True
                    transaction.savepoint_rollback(sid)
                    messages.error(request, "Produk Tidak Boleh Kosong "+ str(e) )
                    pass

                if isFoundError == False:
                    transaction.savepoint_commit(sid)
                    messages.success(request, "data berhasil disimpan")
                else:
                    transaction.get_rollback()
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = FormKoperasi()

    list_data = {

        'side_active'   : 'koper',
        'form'          : form,
        'tables'        : tables,
    }

    return render (request, 'add_kop.html', list_data)


@login_required(login_url=settings.LOGIN_URL)
def upd_kop(request, kop_id):

    tables      = KoperasiModel.objects.get(id = kop_id)
    tb_keu = KeuanganModel.objects.filter(doc_nmkop = kop_id)
    
    paginator   = Paginator(tb_keu, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page_1')
    page_kop    = paginator.get_page(page_number)
    tab_active = 'tab_kop'

    listdptakel      = DPPatuhModel.objects.filter(kat_var__ipkat = 'tata-kelola')
    listdpproris     = DPPatuhModel.objects.filter(kat_var__ipkat = 'profil-risiko')
    listdpall        = DPPatuhModel.objects.filter(kat_var__ipkat = 'tata-kelola') | DPPatuhModel.objects.filter(kat_var__ipkat = 'profil-risiko')

    tab_keu    = KeuanganModel.objects.filter(doc_nmkop = kop_id).order_by('-doc_tahun', '-doc_bulan')[:1]
    if tab_keu:
        form_keu   = FormKeuKoperasi(instance=tab_keu[0])
    else:
        form_keu   = FormKeuKoperasi()



    isFoundError = False

    template = 'upd_kop.html'
    if request.POST:
        form = FormKoperasi(request.POST, request.FILES, instance = tables)
        if form.is_valid():

             with transaction.atomic():
                sid = transaction.savepoint()
                try:
                    post = form.save(commit=False)
                    post.modified_by = str(request.user)
                    jsonstring = request.POST['jenprod']
                    post.save()

                    kopidinstance = KoperasiModel.objects.get(id =kop_id )
                    detailprodkop = ProdukModel.objects.filter(kopid =kop_id )

                    for itemtk in listdpall:
                        detail_dp = None
                        try:
                            detail_dp   = DetailDpPatuh.objects.get(choose_kop = kop_id, choose_dp= itemtk.id)
                        except Exception as e:
                            detail_dp = None

                        dpinstance  = DPPatuhModel.objects.get(id =itemtk.id )
                        valuedp     = request.POST[itemtk.kat_var.ipkat +"_"+itemtk.kat_var.ipsubkat+"-"+str(itemtk.id)]
                        if detail_dp is None :
                            instance_data = [
                                DetailDpPatuh(
                                    choose_dp  = dpinstance,
                                    choose_kop = kopidinstance,
                                    nilai_dp   = int(valuedp)
                                )
                            ]
                            
                            try:
                                DetailDpPatuh.objects.bulk_create(instance_data)
                            except Exception as e:
                                messages.error(request, "Terdapat Kesalahan pada Daftar Kepatuhan")
                                isFoundError = True
                                pass
                          
                        else:
                            detail_dp.choose_dp = dpinstance
                            detail_dp.choose_kop = kopidinstance
                            detail_dp.nilai_dp = int(valuedp)
                            try:
                                detail_dp.save()
                            except Exception as e:
                                isFoundError = True
                                messages.error(request, "Daftar Kepatuhan Gagal Di Ubah")
                                pass
                            
                
                        
                    if jsonstring and isFoundError == False:
                        json_object = json.loads(jsonstring)

                        if len(json_object)== 0  :
                            isFoundError = True
                            messages.error(request, "Produk Tidak Boleh Kosong" )
                        else:
                            for detprod in detailprodkop:
                                found = False
                                idx = 0
                                for jsondata in json_object: 
                                    if jsondata['id'] == detprod.id:
                                        found = True
                                        fieldproduct = ProdukModel.objects.get(id = detprod.id)
                                        fieldproduct.komoditi = request.POST.get('komoditi-'+ str(idx))
                                        fieldproduct.satuan = request.POST.get('satuan-'+ str(idx))
                                        fieldproduct.volume = request.POST.get('volume-'+ str(idx))
                                        fieldproduct.harga = request.POST.get('harga-'+ str(idx))
                                        fieldproduct.total = request.POST.get('total-'+ str(idx))
                                        if request.FILES.get('fotoprod-'+str(idx)): 
                                            fieldproduct.fotoprod = request.FILES.get('fotoprod-'+str(idx))
                                        else:
                                            fieldproduct.fotoprod = fieldproduct.fotoprod
                                        
                                        try:
                                            fieldproduct.save()
                                        except Exception as e:
                                            isFoundError = True
                                            messages.error(request, "Data Gagal Di Ubah,  Terdapat Kesalahan pada Produk")
                                            pass
                                    idx += 1

                                if found == False:
                                    fieldproduct = ProdukModel.objects.get(id = detprod.id)
                                    fieldproduct.delete()


                            for idx,jsondata in enumerate(json_object): 
                                if jsondata['id'] == "":
                                    kom1 = request.POST.get('komoditi-'+ str(idx))
                                    sat1 = request.POST.get('satuan-'+ str(idx))
                                    vol1 = request.POST.get('volume-'+ str(idx))
                                    hrg1 = request.POST.get('harga-'+ str(idx))
                                    tot1 = request.POST.get('total-'+ str(idx))
                                    foto1 = request.FILES.get('fotoprod-'+str(idx))
                                    newprodukdb = ProdukModel(
                                        # komoditi=jsondata['komoditi'],
                                        # satuan=jsondata['satuan'],
                                        # volume=jsondata['volume'],
                                        # harga=jsondata['harga'],
                                        # total=jsondata['total'],
                                        # fotoprod=jsondata['foto'],
                                        komoditi =kom1,
                                        satuan = sat1,
                                        volume = vol1,
                                        harga = hrg1,
                                        total = tot1,
                                        fotoprod = foto1,
                                        kopid=kopidinstance,
                                        )
                                    try:
                                        newprodukdb.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Inputan Produk")
                                        isFoundError = True
                                        pass

                    else:
                        messages.error(request, "Produk Tidak Boleh Kosong" )
                        isFoundError = True

                    if isFoundError==False:  
                        messages.success(request, "Data Berhasil Di Ubah ")
                        transaction.savepoint_commit(sid)
                        return redirect('koper:upd_kop', kop_id)

                except Exception as e:
                    isFoundError = True
                    transaction.get_rollback()
                    messages.error(request, "Produk Tidak Boleh Kosong "+ str(e) )
                    form = FormKoperasi(instance=tables)

                if isFoundError == False:
                    transaction.savepoint_commit(sid)
                    messages.success(request, "data berhasil disimpan")
                else:
                    transaction.get_rollback()
            
        else:
            messages.error(request, "Data Gagal Di Ubah ")
            form = FormKoperasi(instance=tables)
        
    else:
        form = FormKoperasi(instance=tables)

    list_data = {
        'side_active'   : 'koper',
        'form'          : form,
        'form_keu'      : form_keu,
        'dpl_kelola'    : listdptakel,
        'dpl_risiko'    : listdpproris,
        'page_kop'      : page_kop,
        'tables'        : tables,
    }
    return render (request, template, list_data)

def getjsonprodkop(request,kop_id):
    tables_prod = ProdukModel.objects.filter(kopid = kop_id)
    tableobj = list(tables_prod.values())
    list_data = {
        'prod_json'     : tableobj,
    }

    return JsonResponse(list_data, safe= False)

@login_required(login_url=settings.LOGIN_URL)
def del_kop(request, kop_id):
    field = KoperasiModel.objects.filter(id = kop_id)
    fieldproduct = ProdukModel.objects.filter(kopid = kop_id)


    fieldproduct.delete()
    field.delete()

    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('koper:master_kop')



def export_koperasi(request):
    if request.method == 'POST':
        # Get selected option from form
        file_format = request.POST['file-format']
        type = request.POST['file-format']

        koperasi_resource = KoperasiResource()
        dataset = koperasi_resource.export()
        if file_format == 'CSV':
            response = HttpResponse(dataset.csv, content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="koperasi_data.csv"'
            return response        
        elif file_format == 'JSON':
            response = HttpResponse(dataset.json, content_type='application/json')
            response['Content-Disposition'] = 'attachment; filename="koperasi_data.json"'
            return response
        elif file_format == 'XLS (Excel)':
            response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
            response['Content-Disposition'] = 'attachment; filename="koperasi_data.xls"'
            return response   

    return render(request, 'export.html')



@login_required(login_url=settings.LOGIN_URL)
def add_keu_kop(request, kop_id):

    tables = KeuanganModel.objects.all()
    kopinstance = KoperasiModel.objects.get(id = kop_id)

    if request.POST:
        form = FormKeuangan(request.POST, request.FILES)
        if form.is_valid():

            post = form.save(commit=False)
            post.doc_nmkop = kopinstance
            post.created_by = str(request.user)
            post.save()
            form = FormKeuangan()

            messages.success(request, "data berhasil disimpan")
            list_data = {
                'side_active'   : 'koper',
                'form'          : form,
                'tables'        : tables
            }

            return redirect('koper:upd_kop',kop_id)
            # return render(request, "add_keu_kop.html", list_data)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = FormKeuangan()

    list_data = {

        'side_active'   : 'koper',
        'form'          : form,
        'tbkop'          : kopinstance,
        'tables'        : tables,
    }

    return render (request, 'add_keu_kop.html', list_data)



@login_required(login_url=settings.LOGIN_URL)
def upd_keu_kop(request, keu_id, kop_id):

    tables      = KeuanganModel.objects.get(id = keu_id)
    kopinstance = KoperasiModel.objects.get(id = kop_id)

    template = 'upd_keu_kop.html'
    if request.POST:
        form = FormKeuangan(request.POST, request.FILES, instance = tables)
        if form.is_valid():
            post = form.save(commit=False)
            post.doc_nmkop = kopinstance
            post.modified_by = str(request.user)
            post.save()

            messages.success(request, "Data Berhasil Di Ubah")
            return redirect('koper:upd_keu_kop', keu_id, kop_id)
        else:
            messages.error(request, "Data Gagal Di Ubah")
            form = FormKeuangan(instance=tables)
        
    else:
        form = FormKeuangan(instance=tables)

    list_data = {
        'side_active'   : 'koper',
        'form'          : form,
        'tbkop'          : kopinstance,
        'tables'        : tables,
    }
    return render (request, template, list_data)


@login_required(login_url=settings.LOGIN_URL)
def del_keu_kop(request, keu_id, kop_id):
    field = KeuanganModel.objects.filter(id = keu_id)
    field.delete()

    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('koper:upd_kop',kop_id)
