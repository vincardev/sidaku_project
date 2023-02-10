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

@login_required(login_url=settings.LOGIN_URL)
def master_kop(request):
    search =""
    
    tables_1 = KoperasiModel.objects.all()

    if request.GET:
        search = request.GET.get('search')
        query = (Q(title__icontains=search) | Q(kategori__icontains=search) | 
        Q(tahun__icontains=search)) 
        tables_1 = tables_1.filter(query )
    
    list_data = {
        'side_active'   : 'koper',
        'tables_1' : tables_1,
    }

    return render (request, 'master_kop.html', list_data)

@login_required(login_url=settings.LOGIN_URL)
def add_kop(request):

    tables = KoperasiModel.objects.all()
    # if (tables.count() != 0):
    #     return redirect('setting:updsetting', tables[0].id)
    isFoundError = False

    if request.POST:
        form = FormKoperasi(request.POST, request.FILES)
        if form.is_valid():
             with transaction.atomic():
                try:
                    post = form.save(commit=False)
                    post.created_by = str(request.user)
                    jsonstring = request.POST['jenprod']
                    post.save()

                    kopidinstance = KoperasiModel.objects.get(id =post.pk )


                    if jsonstring:
                        json_object = json.loads(jsonstring)

                        if len(json_object)== 0  :
                            isFoundError = True
                            messages.error(request, "Produk Tidak Boleh Kosong" )
                        else:
                            instance_transactions = [
                                ProdukModel(
                                    komoditi=jsondata['komoditi'],
                                    satuan=jsondata['satuan'],
                                    volume=jsondata['volume'],
                                    harga=jsondata['harga'],
                                    total=jsondata['total'],
                                    fotoprod=jsondata['foto'],
                                    kopid=kopidinstance,
                                )
                                for jsondata in json_object
                            ]

                            try:
                                ProdukModel.objects.bulk_create(instance_transactions)
                            except Exception as e:
                                messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Inputan Produk")
                                isFoundError = True
                            
                    else :
                        messages.error(request, "Produk Tidak Boleh Kosong" )
                        isFoundError = True

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
                        return render(request, "add_kop.html", list_data)

                except  Exception as e:
                    messages.error(request, "Produk Tidak Boleh Kosong "+ str(e) )
                    pass
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
    isFoundError = False

    template = 'upd_kop.html'
    if request.POST:
        form = FormKoperasi(request.POST, request.FILES, instance = tables)
        if form.is_valid():

             with transaction.atomic():
                try:
                    post = form.save(commit=False)
                    post.modified_by = str(request.user)
                    jsonstring = request.POST['jenprod']
                    post.save()

                    kopidinstance = KoperasiModel.objects.get(id =kop_id )
                    detailprodkop = ProdukModel.objects.filter(kopid =kop_id )

                    if jsonstring :
                        json_object = json.loads(jsonstring)

                        if len(json_object)== 0  :
                            isFoundError = True
                            messages.error(request, "Produk Tidak Boleh Kosong" )
                            
                        else:
                        

                            for detprod in detailprodkop:
                                found = False
                                for jsondata in json_object: 
                                    if jsondata['id'] == detprod.id:
                                        found = True
                                        fieldproduct = ProdukModel.objects.get(id = detprod.id)
                                        fieldproduct.komoditi = jsondata['komoditi']
                                        fieldproduct.satuan = jsondata['satuan']
                                        fieldproduct.volume = jsondata['volume']
                                        fieldproduct.harga = jsondata['harga']
                                        fieldproduct.total = jsondata['total']
                                        fieldproduct.fotoprod = jsondata['foto'] 
                                        # fieldproduct.save()
                                        try:
                                            fieldproduct.save()
                                        except Exception as e:
                                            isFoundError = True
                                            messages.error(request, "Data Gagal Di Ubah")
                                            pass

                                if found == False:
                                    fieldproduct = ProdukModel.objects.get(id = detprod.id)
                                    fieldproduct.delete()


                            for jsondata in json_object: 
                                if jsondata['id'] == "":
                                    newprodukdb = ProdukModel(
                                        komoditi=jsondata['komoditi'],
                                        satuan=jsondata['satuan'],
                                        volume=jsondata['volume'],
                                        harga=jsondata['harga'],
                                        total=jsondata['total'],
                                        fotoprod=jsondata['foto'],
                                        kopid=kopidinstance,
                                        )
                                    try:
                                        newprodukdb.save()
                                    except Exception as e:
                                        isFoundError = True
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Inputan Produk")
                                        pass

                    else:
                        messages.error(request, "Produk Tidak Boleh Kosong" )
                        isFoundError = True

                    if isFoundError==False:  
                        messages.success(request, "Data Berhasil Di Ubah "+ str(len(json_object)) )
                        return redirect('koper:upd_kop', kop_id)

                except Exception as e:
                    messages.error(request, "Produk Tidak Boleh Kosong "+ str(e) )
                    form = FormKoperasi(instance=tables)

            
        else:
            messages.error(request, "Data Gagal Di Ubah 2")
            form = FormKoperasi(instance=tables)
        
    else:
        form = FormKoperasi(instance=tables)

    list_data = {
        'side_active'   : 'koper',
        'form'          : form,
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

