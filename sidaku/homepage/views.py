from time import strftime
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime

from articles.models import Article
from koperasi.models import KoperasiModel
from keuangan.models import *
from produk.models import *
from umkmdata.models import UmkmModel
from django.http import JsonResponse


# Create your views here.

def index(request):
    headline =  Article.objects.filter(inheadline = True)
    edukasi =  Article.objects.filter(ineducate = True)
    daftarkoperasi =  KoperasiModel.objects.all()
    daftarumkm =  UmkmModel.objects.all()


    allArticle =  Article.objects.filter(inheadline = False,ineducate = False)

    context = {
        "headline": headline,
        "edukasi": edukasi,
        "article": allArticle,
        "allkoperasi":daftarkoperasi,
        "allumkm":daftarumkm,
        "header_menu":"",
        "footer_menu":"",
    }
    return render(request, 'home/index.html', context)


def getkopid(request, kop_id):
    tablekoper     = KoperasiModel.objects.get(id = kop_id)
    tableuang      = KeuanganModel.objects.filter(doc_nmkop = kop_id)
    tableproduk      = ProdukModel.objects.filter(kopid = kop_id)
    template = "home/det_koperasi.html"
    list_data = {
        'lapkeu'       : tableuang,
        'koper'        : tablekoper,
        'prod'        : tableproduk,
    }
    return render (request, template, list_data)

def getumkmid(request, umkm_id):
    tableumkm      = UmkmModel.objects.get(id = umkm_id)
    tableuang      = KeuanganUMKMModel.objects.filter(doc_nmumkm = umkm_id)
    tableproduk    = ProdukUMKM.objects.filter(umkmid = umkm_id)
    tabledemprod   = DetDemandProd.objects.filter(umkmid = umkm_id)
    tabledemsup    = DetDemandSup.objects.filter(umkmid = umkm_id)
    tablepensup    = DetPenilaianSupp.objects.filter(umkmid = umkm_id)
    template = "home/det_umkm.html"
    list_data = {
        'lapkeu'       : tableuang,
        'umkmdat'        : tableumkm,
        'tabledemprod'   : tabledemprod,
        'tabledemsup'    : tabledemsup,
        'tablepensup'    : tablepensup,
        'prod'        : tableproduk,
    }
    return render (request, template, list_data)


def getalldata(request):
    koperasi = KoperasiModel.objects.all()
    umkmdata = UmkmModel.objects.all()
    koperasilist = list(koperasi.values())
    umkmlist = list(umkmdata.values())
    list_data = {
        'koperasi'     : koperasilist,
        'umkmdata'     : umkmlist,
    }

    return JsonResponse(list_data, safe= False)