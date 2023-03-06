from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.db.models import Q
from django.contrib import messages
from produk.models import *
from umkmdata.forms import FormUMKM
from produk.forms import *
from umkmdata.forms import *
from umkmdata.models import *

from django.db import transaction
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator

import json


from .resources import *
from django.http import HttpResponse
from tablib import Dataset

@login_required(login_url=settings.LOGIN_URL)
def master_umkm(request):
    search =""
    
    tables = UmkmModel.objects.all()

    if request.GET:
        search = request.GET.get('search')
        query = (Q(pu_nmpmlk__icontains=search) | Q(pu_aldmisi__icontains=search) | 
        Q(pu_noaggta__icontains=search) | Q(pu_noktp__icontains=search) | Q(pu_noktp__icontains=search) |
        Q(du_nmusha__icontains=search)  ) 
        tables = tables.filter(query )

    if request.POST:
        # Get selected option from form
        file_format = request.POST['file-format']
        post_type = request.POST['post-type']

        if post_type == 'Export':
            umkm_resource = UMKMResource()
            dataset = umkm_resource.export()
            if file_format == 'CSV':
                response = HttpResponse(dataset.csv, content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="umkm_data.csv"'
                return response        
            elif file_format == 'JSON':
                response = HttpResponse(dataset.json, content_type='application/json')
                response['Content-Disposition'] = 'attachment; filename="umkm_data.json"'
                return response
            elif file_format == 'XLS (Excel)':
                response = HttpResponse(dataset.xlsx, content_type='application/vnd.ms-excel')
                response['Content-Disposition'] = 'attachment; filename="umkm_data.xlsx"'
                return response   
        
        if post_type == 'Import':
            umkm_resource = UMKMResource()
            dataset = Dataset()
            new_umkm = request.FILES['importData']

            if file_format == 'XLS (Excel)':
                imported_data = dataset.load(new_umkm.read(),format='xlsx')
                result = umkm_resource.import_data(dataset, dry_run=True, raise_errors=True)                                                                 
            elif file_format == 'CSV':
                imported_data = dataset.load(new_umkm.read().decode('utf-8'),format='csv')
                result = umkm_resource.import_data(dataset, dry_run=True, raise_errors=True)                                                                 
            elif file_format == 'JSON':
                imported_data = dataset.load(new_umkm.read().decode('utf-8'),format='json')
                # Testing data import
                result = umkm_resource.import_data(dataset, dry_run=True, raise_errors=True) 

            if not result.has_errors():
                # Import now
                umkm_resource.import_data(dataset, dry_run=False)


    paginator   = Paginator(tables, 10) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    list_data = {
        'side_active'   : 'umkmdat',
        'tables' : tables,
        'page_obj' : page_obj,
        'search' : search,
    }

    return render (request, 'master_umkm.html', list_data)



@login_required(login_url=settings.LOGIN_URL)
def add_umkm(request):
    isFoundError = False
    tables = UmkmModel.objects.all()
    formprodumkm = FormProdukUMKM()
    formdemprod = FormDemandProdUMKM()
    formdemsupp = FormDemandSuppUMKM()
    formpensupp = FormNilaiSuppUMKM()
    formtngkrj  = FormTenagaKerjaUMKM()
    formperijinan  = FormPerijinanUMKM()
    formenergi  = FormSumEnergiUMKM()
    formbahanbaku  = FormBahanBakuUMKM()
    formdetmesin  = FormDetailMesinUMKM()
    formdetfas  = FormDetailFasilitasUMKM()
    formdetpelat  = FormDetailPelatihanUMKM()
    # if (tables.count() != 0):
    #     return redirect('setting:updsetting', tables[0].id)
    idprimarykey =""
    if request.POST:
        form = FormUMKM(request.POST, request.FILES)
        if form.is_valid():
            # du_btkusha = form.cleaned_data.get('du_btkusha')
            # du_bdgusha = form.cleaned_data.get('du_bdgusha')
            with transaction.atomic():
                sid = transaction.savepoint()
                try:
                    post = form.save(commit=False)
                    post.created_by = str(request.user)
                    jsstr_prod = request.POST['jenprod']
                    jsstr_demprod = request.POST['demprod']
                    jsstr_demsupp = request.POST['demsupp']
                    jsstr_pensupp = request.POST['pensupp']
                    jsstr_tngkrj = request.POST['tngkrj']
                    jsstr_dataijin = request.POST['dataijin']
                    jsstr_bhbaku = request.POST['databhbaku']
                    jsstr_dtenergi = request.POST['dataenergi']
                    jsstr_dtmesin = request.POST['datamesin']
                    jsstr_fasildat = request.POST['fasildata']
                    jsstr_pelatdat = request.POST['pelatdata']
                    
                    post.save()
                    idprimarykey= post.pk

                    umkmidinstance = UmkmModel.objects.get(id =post.pk )

                    if jsstr_prod:
                        jsload_prod = json.loads(jsstr_prod)
                        if len(jsload_prod) ==  0  :
                            isFoundError = True
                            messages.error(request, "Produk Tidak Boleh Kosong" )
                        else:
                            instance_produkumkm = [
                                ProdukUMKM(
                                    # komoditi=jsonprod['komoditi'],
                                    # satuan=jsonprod['satuan'],
                                    # volume=jsonprod['volume'],
                                    # harga=jsonprod['harga'],
                                    # total=jsonprod['total'],
                                    # fotoprod=jsonprod['foto'],

                                    komoditi = request.POST.get('komoditi-'+ str(idx)),
                                    satuan = request.POST.get('satuan-'+ str(idx)),
                                    volume = request.POST.get('volume-'+ str(idx)),
                                    harga = request.POST.get('harga-'+ str(idx)),
                                    total = request.POST.get('total-'+ str(idx)),
                                    fotoprod = request.FILES.get('fotoprod-'+str(idx)),
                                    umkmid=umkmidinstance,
                                )
                                for idx, jsonprod in enumerate(jsload_prod)
                                
                            ]
                            try:
                                ProdukUMKM.objects.bulk_create(instance_produkumkm)
                            except Exception as e:
                                messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Produk")
                                isFoundError = True
                                pass
                    else:
                        isFoundError = True
                        messages.error(request, "Produk Tidak Boleh Kosong" )
                    
                    if jsstr_demprod and isFoundError == False:
                        jsload_demprod = json.loads(jsstr_demprod)
                        instance_demprod = [
                            DetDemandProd(
                                dpd_nmprod=jsondata['dpd_nmprod'],
                                dpd_bulan=jsondata['dpd_bulan'],
                                dpd_tahun=jsondata['dpd_tahun'],
                                dpd_demand=jsondata['dpd_demand'],
                                dpd_produksi=jsondata['dpd_produksi'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_demprod
                        ]
                        try:
                            DetDemandProd.objects.bulk_create(instance_demprod)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Permintaan Produk")
                            isFoundError = True
                            pass
                           
                    if jsstr_demsupp and isFoundError == False:
                        jsload_demsupp = json.loads(jsstr_demsupp)
                        instance_demsupp = [
                            DetDemandSup(
                                dsp_jensup=jsondata['dsp_jensup'],
                                dsp_bulan=jsondata['dsp_bulan'],
                                dsp_tahun=jsondata['dsp_tahun'],
                                dsp_demand=jsondata['dsp_demand'],
                                dsp_produksi=jsondata['dsp_produksi'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_demsupp
                        ]
                        try:
                            DetDemandSup.objects.bulk_create(instance_demsupp)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Permintaan Supplier")
                            isFoundError = True
                            pass

                    if jsstr_pensupp and isFoundError == False:
                        jsload_pensupp = json.loads(jsstr_pensupp)
                        instance_pensupp = [
                            DetPenilaianSupp(
                                dps_nm_supp=jsondata['dps_nm_supp'],
                                dps_kualitas=jsondata['dps_kualitas'],
                                dps_pengiriman=jsondata['dps_pengiriman'],
                                dps_harga=jsondata['dps_harga'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_pensupp
                        ]
                        try:
                            DetPenilaianSupp.objects.bulk_create(instance_pensupp)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Penilaian Pemasok")
                            isFoundError = True
                            pass

                    if jsstr_tngkrj and isFoundError == False:
                        jsload_tngkrj = json.loads(jsstr_tngkrj)
                        instance_tngkrj = [
                            DetailTenagaKerja(
                                jenis_tngkrj=JenisTenagaKerja.objects.get(id =jsondata['jenis_tngkrj']) ,
                                jml_org=jsondata['jml_org'],
                                pendidikan=Pendidikan.objects.get(id =jsondata['pendidikan']),
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_tngkrj
                        ]
                        try:
                            DetailTenagaKerja.objects.bulk_create(instance_tngkrj)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Tenaga Kerja")
                            isFoundError = True
                            pass

                    if jsstr_dataijin and isFoundError == False:
                        jsload_dtijin = json.loads(jsstr_dataijin)
                        instance_perijin = [
                            DetailPerijinan(
                                tipe_ijin=TipePerijinan.objects.get(id =jsondata['tipe_ijin']),
                                no_ijin=jsondata['no_ijin'],
                                tgl_ijin=jsondata['tgl_ijin'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_dtijin
                        ]
                        try:
                            DetailPerijinan.objects.bulk_create(instance_perijin)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Perijinan")
                            isFoundError = True
                            pass

                    if jsstr_bhbaku and isFoundError == False:
                        jsload_bhbaku = json.loads(jsstr_bhbaku)
                        instance_bhbaku = [
                            DetailBahanBaku(
                                jen_bhbaku=jsondata['jen_bhbaku'],
                                volume=jsondata['volume'],
                                nilai=jsondata['nilai'],
                                asalBB=jsondata['asalBB'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_bhbaku
                        ]
                        try:
                            DetailBahanBaku.objects.bulk_create(instance_bhbaku)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Bahan Baku")
                            isFoundError = True
                            pass

                    if jsstr_dtenergi and isFoundError == False:
                        jsload_dtenergi = json.loads(jsstr_dtenergi)
                        instance_energi = [
                            DetailEnergi(
                                jen_energi=JenisEnergi.objects.get(id =jsondata['jen_energi']),
                                kapasitas=jsondata['kapasitas'],
                                keterangan=jsondata['keterangan'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_dtenergi
                        ]

                        try:
                            DetailEnergi.objects.bulk_create(instance_energi)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Energi")
                            isFoundError = True
                            pass

                    if jsstr_dtmesin and isFoundError == False:
                        jsload_dtmesin = json.loads(jsstr_dtmesin)
                        instance_mesin = [
                            DetailMesin(
                                nm_mesin=jsondata['nm_mesin'],
                                desc_mesin=jsondata['desc_mesin'],
                                jml_mesin=jsondata['jml_mesin'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_dtmesin
                        ]
                        try:
                            DetailMesin.objects.bulk_create(instance_mesin)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Mesin/Alat")
                            isFoundError = True
                            pass

                    if jsstr_fasildat and isFoundError == False:
                        jsload_fasildat = json.loads(jsstr_fasildat)
                        instance_fasil = [
                            
                            DetailFasilitas(
                                tipe_fasi=TipeFasilitas.objects.get(id =jsondata['tipe_fasi']),
                                nm_fasi=jsondata['nm_fasi'],
                                thn_fasi=jsondata['thn_fasi'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_fasildat
                                
                        ]
                        try:
                            DetailFasilitas.objects.bulk_create(instance_fasil)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Fasilitas")
                            isFoundError = True
                            pass

                    if jsstr_pelatdat and isFoundError == False:
                        jsload_pelatdat = json.loads(jsstr_pelatdat)
                        instance_pelat = [
                            DetailPelatihan(
                                nm_pelat=jsondata['nm_pelat'],
                                tmpt_pelat=jsondata['tmpt_pelat'],
                                thn_pelat=jsondata['thn_pelat'],
                                umkmid=umkmidinstance,
                            )
                            for jsondata in jsload_pelatdat
                        ]
                        try:
                            DetailPelatihan.objects.bulk_create(instance_pelat)
                        except Exception as e:
                            messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Pelatihan")
                            isFoundError = True
                            pass
                     

                except Exception as e :
                    isFoundError = True
                    transaction.savepoint_rollback(sid)
                    messages.error(request, e.args)
                    messages.error(request, "data gagal disimpan")


                if isFoundError == False:
                    transaction.savepoint_commit(sid)
                    messages.success(request, "data berhasil disimpan")
                else:
                    transaction.get_rollback()

            # form = FormUMKM()

            # messages.success(request,  test)
            list_data = {
                'side_active'     : 'umkm',
                'form'            : form,
                'form_pdumkm'     : formprodumkm,
                'form_demprod'    : formdemprod,
                'form_demsupp'    : formdemsupp,
                'form_pensupp'    : formpensupp,
                'form_tngkrj'     : formtngkrj,
                'form_perijin'    : formperijinan,
                'form_energi'     : formenergi,
                'form_bahanbaku'  : formbahanbaku,
                'form_detmesin'  : formdetmesin,
                'form_detfasil'  : formdetfas,
                'form_detpelat'  : formdetpelat,
                'tables'          : tables
            }

            # return redirect('koper:add_kop', post.pk)
            if isFoundError == True:
                transaction.get_rollback()
                messages.error(request, "Data Gagal Di Ubah, Silahkan Cek Kembali Data yang telah di Inputkan")
            else:
                transaction.savepoint_commit(sid)
                return redirect('umkmdat:upd_umkm', idprimarykey)
                # return render(request, "add_umkm.html", list_data)
        else:
            messages.error(request, "data gagal disimpan")

    else:
        form = FormUMKM()

    list_data = {

        'side_active'    : 'umkmdat',
        'form'           : form,
        'form_pdumkm'    : formprodumkm,
        'form_demprod'   : formdemprod,
        'form_demsupp'   : formdemsupp,
        'form_pensupp'   : formpensupp,
        'form_tngkrj'    : formtngkrj,
        'form_perijin'   : formperijinan,
        'form_energi'    : formenergi,
        'form_bahanbaku' : formbahanbaku,
        'form_detmesin'  : formdetmesin,
        'form_detfasil'  : formdetfas,
        'form_detpelat'  : formdetpelat,
        'tables'         : tables,
    }

    return render (request, 'add_umkm.html', list_data)


@login_required(login_url=settings.LOGIN_URL)
def upd_umkm(request, umkm_id):

    tables      = UmkmModel.objects.get(id = umkm_id)

    formprodumkm = FormProdukUMKM()
    formdemprod = FormDemandProdUMKM()
    formdemsupp = FormDemandSuppUMKM()
    formpensupp = FormNilaiSuppUMKM()
    formtngkrj  = FormTenagaKerjaUMKM()
    formperijinan  = FormPerijinanUMKM()
    formenergi  = FormSumEnergiUMKM()
    formbahanbaku  = FormBahanBakuUMKM()
    formdetmesin  = FormDetailMesinUMKM()
    formdetfas  = FormDetailFasilitasUMKM()
    formdetpelat  = FormDetailPelatihanUMKM()
    

    template = 'upd_umkm.html'
    if request.POST:
        form = FormUMKM(request.POST, request.FILES, instance = tables)
        if form.is_valid():
            with transaction.atomic():
                sid = transaction.savepoint()
                try:
                    post = form.save(commit=False)
                    post.modified_by = str(request.user)
                    jsstr_prod = request.POST['jenprod']
                    jsstr_demprod = request.POST['demprod']
                    jsstr_demsupp = request.POST['demsupp']
                    jsstr_pensupp = request.POST['pensupp']
                    jsstr_tngkrj = request.POST['tngkrj']
                    jsstr_dataijin = request.POST['dataijin']
                    jsstr_bhbaku = request.POST['databhbaku']
                    jsstr_dtenergi = request.POST['dataenergi']
                    jsstr_dtmesin = request.POST['datamesin']
                    jsstr_fasildat = request.POST['fasildata']
                    jsstr_pelatdat = request.POST['pelatdata']

                        
                    jsload_demprod = json.loads(jsstr_demprod)
                    jsload_demsupp = json.loads(jsstr_demsupp)
                    jsload_pensupp = json.loads(jsstr_pensupp)
                    jsload_tngkrj = json.loads(jsstr_tngkrj)
                    jsload_dtijin = json.loads(jsstr_dataijin)
                    jsload_bhbaku = json.loads(jsstr_bhbaku)
                    jsload_dtenergi = json.loads(jsstr_dtenergi)
                    jsload_dtmesin = json.loads(jsstr_dtmesin)
                    jsload_fasildat = json.loads(jsstr_fasildat)
                    jsload_pelatdat = json.loads(jsstr_pelatdat)
                    post.save()

                    umkmidinstance = UmkmModel.objects.get(id =umkm_id )
                    detprodumkm = ProdukUMKM.objects.filter(umkmid =umkm_id )
                    detdemprod  = DetDemandProd.objects.filter(umkmid =umkm_id )
                    detdemsupp  = DetDemandSup.objects.filter(umkmid =umkm_id )
                    detpensupp  = DetPenilaianSupp.objects.filter(umkmid =umkm_id )
                    dettngkerja = DetailTenagaKerja.objects.filter(umkmid =umkm_id )
                    detperijin  = DetailPerijinan.objects.filter(umkmid =umkm_id )
                    detbhbaku   = DetailBahanBaku.objects.filter(umkmid =umkm_id )
                    detenergi   = DetailEnergi.objects.filter(umkmid =umkm_id )
                    detMesin    = DetailMesin.objects.filter(umkmid =umkm_id )
                    detFasil    = DetailFasilitas.objects.filter(umkmid =umkm_id )
                    detPelat    = DetailPelatihan.objects.filter(umkmid =umkm_id )

                    isFoundError = False

                    if jsstr_prod and isFoundError == False:
                        jsload_prod = json.loads(jsstr_prod)
                        if len(jsload_prod)== 0  :
                            isFoundError = True
                            messages.error(request, "Produk Tidak Boleh Kosong" )
                            
                        else:
                            for fieldumkm in detprodumkm:
                                found = False
                                idx = 0
                                for jsondata in jsload_prod: 
                                    if jsondata['id'] == fieldumkm.id:
                                        found = True
                                        fieldproduct = ProdukUMKM.objects.get(id = fieldumkm.id)
                                        fieldproduct.komoditi = request.POST.get('komoditi-'+ str(idx))
                                        fieldproduct.satuan = request.POST.get('satuan-'+ str(idx))
                                        fieldproduct.volume = request.POST.get('volume-'+ str(idx))
                                        fieldproduct.harga = request.POST.get('harga-'+ str(idx))
                                        fieldproduct.total = request.POST.get('total-'+ str(idx))
                                        if request.FILES.get('fotoprod-'+str(idx)): 
                                            fieldproduct.fotoprod = request.FILES.get('fotoprod-'+str(idx))
                                        else:
                                            fieldproduct.fotoprod = fieldproduct.fotoprod
                                        # fieldproduct.komoditi = jsondata['komoditi']
                                        # fieldproduct.satuan = jsondata['satuan']
                                        # fieldproduct.volume = jsondata['volume']
                                        # fieldproduct.harga = jsondata['harga']
                                        # fieldproduct.total = jsondata['total']
                                        # fieldproduct.fotoprod = jsondata['foto'] 
                                        # fieldproduct.save()
                                        try:
                                            fieldproduct.save()
                                        except Exception as e:
                                            messages.error(request, "Data Gagal Di Ubah,  Terdapat Kesalahan pada Produk")
                                            isFoundError = True
                                            pass
                                    idx += 1

                                if found == False:
                                    fieldproduct = ProdukUMKM.objects.get(id = fieldumkm.id)
                                    fieldproduct.delete()
                            
                            for idx,jsondata in  enumerate(jsload_prod): 
                                if jsondata['id'] == "":
                                    kom1 = request.POST.get('komoditi-'+ str(idx))
                                    sat1 = request.POST.get('satuan-'+ str(idx))
                                    vol1 = request.POST.get('volume-'+ str(idx))
                                    hrg1 = request.POST.get('harga-'+ str(idx))
                                    tot1 = request.POST.get('total-'+ str(idx))
                                    foto1 = request.FILES.get('fotoprod-'+str(idx))
                                    newprodukdb = ProdukUMKM(
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
                                        umkmid=umkmidinstance,
                                        )
                                    try:
                                        newprodukdb.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Produk")
                                        isFoundError = True
                                        pass
                        
                    if (isFoundError == False):
                        for fieldata in detdemprod:
                            found = False
                            for jsondata in jsload_demprod: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fieldtab = DetDemandProd.objects.get(id = fieldata.id)
                                    fieldtab.dpd_nmprod = jsondata['dpd_nmprod']
                                    fieldtab.dpd_bulan = jsondata['dpd_bulan']
                                    fieldtab.dpd_tahun = jsondata['dpd_tahun']
                                    fieldtab.dpd_demand = jsondata['dpd_demand']
                                    fieldtab.dpd_produksi = jsondata['dpd_produksi']
                                    # fieldproduct.save()
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Permintaan Produk")
                                        isFoundError = True
                                        pass


                            if found == False:
                                fieldtab = DetDemandProd.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for fieldata in detdemsupp:
                            found = False
                            for jsondata in jsload_demsupp: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fieldtab = DetDemandSup.objects.get(id = fieldata.id)
                                    fieldtab.dsp_jensup = jsondata['dsp_jensup']
                                    fieldtab.dsp_bulan = jsondata['dsp_bulan']
                                    fieldtab.dsp_tahun = jsondata['dsp_tahun']
                                    fieldtab.dsp_demand = jsondata['dsp_demand']
                                    fieldtab.dsp_produksi = jsondata['dsp_produksi']
                                    # fieldproduct.save()
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Permintaan Pemasok")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetDemandSup.objects.get(id = fieldata.id)
                                fieldtab.delete()


                    if (isFoundError == False):
                        for fieldata in detpensupp:
                            found = False
                            for jsondata in jsload_pensupp: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fieldtab = DetPenilaianSupp.objects.get(id = fieldata.id)
                                    fieldtab.dps_nm_supp = jsondata['dps_nm_supp']
                                    fieldtab.dps_kualitas = jsondata['dps_kualitas']
                                    fieldtab.dps_pengiriman = jsondata['dps_pengiriman']
                                    fieldtab.dps_harga = jsondata['dps_harga']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan Pada Penilaian Pemasok")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetPenilaianSupp.objects.get(id = fieldata.id)
                                fieldtab.delete()


                    if (isFoundError == False):
                        for fieldata in dettngkerja:
                            found = False
                            for jsondata in jsload_tngkrj: 
                                if jsondata['id'] == fieldata.id:
                                    found = True

                                    tenaga_instance = JenisTenagaKerja.objects.get(id = jsondata['jenis_tngkrj'])
                                    pend_instance = Pendidikan.objects.get(id = jsondata['pendidikan'] )
                                    fieldtab = DetailTenagaKerja.objects.get(id = fieldata.id)
                                    fieldtab.jenis_tngkrj = tenaga_instance
                                    fieldtab.jml_org = jsondata['jml_org']
                                    fieldtab.pendidikan = pend_instance
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Tenaga Kerja")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailTenagaKerja.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for fieldata in detperijin:
                            found = False
                            for jsondata in jsload_dtijin: 
                                if jsondata['id'] == fieldata.id:
                                    found = True

                                    ijin_instance = TipePerijinan.objects.get(id =jsondata['tipe_ijin'])
                                    fieldtab = DetailPerijinan.objects.get(id = fieldata.id)
                                    fieldtab.tipe_ijin = ijin_instance
                                    fieldtab.no_ijin = jsondata['no_ijin']
                                    fieldtab.tgl_ijin = jsondata['tgl_ijin']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahab pada Daftar Perijinan")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailPerijinan.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for fieldata in detbhbaku:
                            found = False
                            for jsondata in jsload_bhbaku: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fieldtab = DetailBahanBaku.objects.get(id = fieldata.id)
                                    fieldtab.jen_bhbaku = jsondata['jen_bhbaku']
                                    fieldtab.volume = jsondata['volume']
                                    fieldtab.nilai = jsondata['nilai']
                                    fieldtab.asalBB = jsondata['asalBB']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Deftar Bahan Baku")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailBahanBaku.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for fieldata in detenergi:
                            found = False
                            for jsondata in jsload_dtenergi: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    energi_instance = JenisEnergi.objects.get(id =jsondata['jen_energi'])
                                    fieldtab = DetailEnergi.objects.get(id = fieldata.id)
                                    fieldtab.jen_energi = energi_instance
                                    fieldtab.kapasitas = jsondata['kapasitas']
                                    fieldtab.keterangan = jsondata['keterangan']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Energi")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailEnergi.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for fieldata in detMesin:
                            found = False
                            for jsondata in jsload_dtmesin: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fieldtab = DetailMesin.objects.get(id = fieldata.id)
                                    fieldtab.nm_mesin = jsondata['nm_mesin']
                                    fieldtab.desc_mesin = jsondata['desc_mesin']
                                    fieldtab.jml_mesin = jsondata['jml_mesin']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Mesin")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailMesin.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for fieldata in detFasil:
                            found = False
                            for jsondata in jsload_fasildat: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fasil_instance = TipeFasilitas.objects.get(id =jsondata['tipe_fasi'])
                                    fieldtab = DetailFasilitas.objects.get(id = fieldata.id)
                                    fieldtab.tipe_fasi = fasil_instance
                                    fieldtab.nm_fasi = jsondata['nm_fasi']
                                    fieldtab.thn_fasi = jsondata['thn_fasi']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Fasilitas")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailFasilitas.objects.get(id = fieldata.id)
                                fieldtab.delete()
                    if (isFoundError == False):
                        for fieldata in detPelat:
                            found = False
                            for jsondata in jsload_pelatdat: 
                                if jsondata['id'] == fieldata.id:
                                    found = True
                                    fieldtab = DetailPelatihan.objects.get(id = fieldata.id)
                                    fieldtab.nm_pelat = jsondata['nm_pelat']
                                    fieldtab.tmpt_pelat = jsondata['tmpt_pelat']
                                    fieldtab.thn_pelat = jsondata['thn_pelat']
                                    
                                    try:
                                        fieldtab.save()
                                    except Exception as e:
                                        messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Pelatihan")
                                        isFoundError = True
                                        pass

                            if found == False:
                                fieldtab = DetailPelatihan.objects.get(id = fieldata.id)
                                fieldtab.delete()

                    if (isFoundError == False):
                        for jsondata in jsload_demprod: 
                            if jsondata['id'] == "":
                                newdatadb = DetDemandProd(
                                    dpd_nmprod=jsondata['dpd_nmprod'],
                                    dpd_bulan=jsondata['dpd_bulan'],
                                    dpd_tahun=jsondata['dpd_tahun'],
                                    dpd_demand=jsondata['dpd_demand'],
                                    dpd_produksi=jsondata['dpd_produksi'],
                                    umkmid=umkmidinstance,
                                    )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Permintaan Produk")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_demsupp: 
                            if jsondata['id'] == "":
                                newdatadb = DetDemandSup(
                                    dsp_jensup=jsondata['dsp_jensup'],
                                    dsp_bulan=jsondata['dsp_bulan'],
                                    dsp_tahun=jsondata['dsp_tahun'],
                                    dsp_demand=jsondata['dsp_demand'],
                                    dsp_produksi=jsondata['dsp_produksi'],
                                    umkmid=umkmidinstance,
                                    )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Permintaan Pemasok")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_pensupp: 
                            if jsondata['id'] == "":
                                newdatadb = DetPenilaianSupp(
                                    dps_nm_supp=jsondata['dps_nm_supp'],
                                    dps_kualitas=jsondata['dps_kualitas'],
                                    dps_pengiriman=jsondata['dps_pengiriman'],
                                    dps_harga=jsondata['dps_harga'],
                                    umkmid=umkmidinstance,
                                    )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Penilaian Pemasok")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_tngkrj: 
                            if jsondata['id'] == "":

                                tenaga_instance = JenisTenagaKerja.objects.get(id =int(jsondata['jenis_tngkrj']))
                                pend_instance = Pendidikan.objects.get(id =int(jsondata['pendidikan']))
                                newdatadb =  DetailTenagaKerja(
                                    jenis_tngkrj=tenaga_instance,
                                    jml_org=jsondata['jml_org'],
                                    pendidikan=pend_instance,
                                    umkmid=umkmidinstance,
                                    )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Tenaga Kerja")
                                    isFoundError = True
                                    pass
                    
                    if (isFoundError == False):
                        for jsondata in jsload_dtijin: 
                            if jsondata['id'] == "":
                                ijin_instance = TipePerijinan.objects.get(id =jsondata['tipe_ijin'])
                                newdatadb =  DetailPerijinan(
                                    tipe_ijin=ijin_instance,
                                    no_ijin=jsondata['no_ijin'],
                                    tgl_ijin=jsondata['tgl_ijin'],
                                    umkmid=umkmidinstance,
                                    )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Perijinan")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_bhbaku: 
                            if jsondata['id'] == "":
                                newdatadb =  DetailBahanBaku(
                                    jen_bhbaku=jsondata['jen_bhbaku'],
                                    volume=jsondata['volume'],
                                    nilai=jsondata['nilai'],
                                    asalBB=jsondata['asalBB'],
                                    umkmid=umkmidinstance,
                                )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Bahan Baku")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):     
                        for jsondata in jsload_dtenergi: 
                            if jsondata['id'] == "":
                                energi_instance = JenisEnergi.objects.get(id =jsondata['jen_energi'])
                                newdatadb =  DetailEnergi(
                                    jen_energi=energi_instance,
                                    kapasitas=jsondata['kapasitas'],
                                    keterangan=jsondata['keterangan'],
                                    umkmid=umkmidinstance,
                                )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Energi")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_dtmesin: 
                            if jsondata['id'] == "":
                                newdatadb =  DetailMesin(
                                    nm_mesin=jsondata['nm_mesin'],
                                    desc_mesin=jsondata['desc_mesin'],
                                    jml_mesin=jsondata['jml_mesin'],
                                    umkmid=umkmidinstance,
                                    )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Mesin")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_fasildat: 
                            if jsondata['id'] == "":
                                fasil_instance = TipeFasilitas.objects.get(id =jsondata['tipe_fasi'])
                                newdatadb =  DetailFasilitas(
                                    tipe_fasi=fasil_instance,
                                    nm_fasi=jsondata['nm_fasi'],
                                    thn_fasi=jsondata['thn_fasi'],
                                    umkmid=umkmidinstance,
                                )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Fasilitas")
                                    isFoundError = True
                                    pass

                    if (isFoundError == False):
                        for jsondata in jsload_pelatdat: 
                            if jsondata['id'] == "":
                                newdatadb =  DetailPelatihan(
                                    nm_pelat=jsondata['nm_pelat'],
                                    tmpt_pelat=jsondata['tmpt_pelat'],
                                    thn_pelat=jsondata['thn_pelat'],
                                    umkmid=umkmidinstance,
                                )
                                try:
                                    newdatadb.save()
                                except Exception as e:
                                    messages.error(request, "Data Gagal Di Ubah, Terdapat Kesalahan pada Daftar Pelatihan")
                                    isFoundError = True
                                    pass

                    if isFoundError == False:
                        messages.success(request, "Data Berhasil Di Ubah")
                        transaction.savepoint_commit(sid)
                        return redirect('umkmdat:upd_umkm', umkm_id)
                    else:
                        isFoundError = True
                        messages.error(request, "Silahkan Cek Kembali Data yang telah di Inputkan")

                except Exception as e:
                    # print(e)
                    isFoundError = True
                    transaction.savepoint_rollback(sid)
                    form = FormUMKM(instance=tables)
                    messages.error(request, "Data Gagal Di Ubah,Silahkan Cek Kembali Data yang telah di Inputkan <br>" + e)
                
                if isFoundError == False:
                    transaction.savepoint_commit(sid)
                    messages.success(request, "data berhasil disimpan")
                else:
                    transaction.get_rollback()
        else:
            messages.error(request, "Data Gagal Di Ubah, Silahkan Cek Kembali Data yang telah di Inputkan")
            form = FormUMKM(instance=tables)
        
    else:
        form = FormUMKM(instance=tables)

    list_data = {
        'side_active'   : 'umkmdat',
        'form'          : form,
        'form_pdumkm'    : formprodumkm,
        'form_demprod'   : formdemprod,
        'form_demsupp'   : formdemsupp,
        'form_pensupp'   : formpensupp,
        'form_tngkrj'    : formtngkrj,
        'form_perijin'   : formperijinan,
        'form_energi'    : formenergi,
        'form_bahanbaku' : formbahanbaku,
        'form_detmesin'  : formdetmesin,
        'form_detfasil'  : formdetfas,
        'form_detpelat'  : formdetpelat,
        'tables'        : tables,
    }
    return render (request, template, list_data)



@login_required(login_url=settings.LOGIN_URL)
def del_umkm(request, umkm_id):
    field = UmkmModel.objects.filter(id = umkm_id)
    fieldproduct = ProdukUMKM.objects.filter(umkmid = umkm_id)
    fielddemprod = DetDemandProd.objects.filter(umkmid = umkm_id)
    fielddemsupp = DetDemandSup.objects.filter(umkmid = umkm_id)
    fieldbhbk    = DetailBahanBaku.objects.filter(umkmid = umkm_id)
    fieldenergi  = DetailEnergi.objects.filter(umkmid = umkm_id)
    fieldfasil   = DetailFasilitas.objects.filter(umkmid = umkm_id)
    fieldmsn     = DetailMesin.objects.filter(umkmid = umkm_id)
    fieldpelat   = DetailPelatihan.objects.filter(umkmid = umkm_id)
    fieldijin    = DetailPerijinan.objects.filter(umkmid = umkm_id)
    fieldtngkj   = DetailTenagaKerja.objects.filter(umkmid = umkm_id)
    fielpensupp  = DetPenilaianSupp.objects.filter(umkmid = umkm_id)


    fieldbhbk.delete()
    fieldenergi.delete()
    fieldfasil.delete()
    fieldmsn.delete()
    fieldpelat.delete()
    fieldijin.delete()
    fieldtngkj.delete()
    fielddemprod.delete()
    fielddemsupp.delete()
    fieldproduct.delete()
    fielpensupp.delete()
    field.delete()

    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('umkmdat:master_umkm')




def getjsontable(request,umkm_id):
    field_prod = ProdukUMKM.objects.filter(umkmid = umkm_id)
    fielddemprod = DetDemandProd.objects.filter(umkmid = umkm_id)
    fielddemsupp = DetDemandSup.objects.filter(umkmid = umkm_id)
    fieldbhbk    = DetailBahanBaku.objects.filter(umkmid = umkm_id)
    fieldenergi  = DetailEnergi.objects.filter(umkmid = umkm_id)
    fieldfasil   = DetailFasilitas.objects.filter(umkmid = umkm_id)
    fieldmsn     = DetailMesin.objects.filter(umkmid = umkm_id)
    fieldpelat   = DetailPelatihan.objects.filter(umkmid = umkm_id)
    fieldijin    = DetailPerijinan.objects.filter(umkmid = umkm_id)
    fieldtngkj   = DetailTenagaKerja.objects.filter(umkmid = umkm_id)
    fielpensupp  = DetPenilaianSupp.objects.filter(umkmid = umkm_id)

    # tableprod = list(tables_prod.values())
   
    list_data = {
        'prod_json'     : list(field_prod.values()),
        'demprod_json'  : list(fielddemprod.values()),
        'demsupp_json'  : list(fielddemsupp.values()),
        'bhbaku_json'   : list(fieldbhbk.values()),
        'energi_json'   : list(fieldenergi.values()),
        'fasil_json'    : list(fieldfasil.values()),
        'mesin_json'    : list(fieldmsn.values()),
        'pelat_json'    : list(fieldpelat.values()),
        'ijin_json'     : list(fieldijin.values()),
        'tngkerja_json' : list(fieldtngkj.values()),
        'pensupp_json'  : list(fielpensupp.values()),
    }

    return JsonResponse(list_data, safe= False)



def getjsonproduk(request,prod_id):
    field_prod = ProdukUMKM.objects.get(id = prod_id)
   
    # tableprod = list(tables_prod.values())
   
    list_data = {
        'prod_url'     : field_prod.fotoprod.url,
    }

    return JsonResponse(list_data, safe= False)