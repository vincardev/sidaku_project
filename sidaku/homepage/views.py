from time import strftime
from django.shortcuts import render
from django.db.models import Q
from datetime import datetime

from articles.models import Article
from koperasi.models import KoperasiModel
from keuangan.models import *
from produk.models import *
from articles.models import ArticleSeries
from regulasi.models import RegulasiModel
from umkmdata.models import BidangUsaha
from umkmdata.models import UmkmModel
from django.http import JsonResponse
from django.core.paginator import Paginator

from companysetup.forms import *

from django.contrib import messages


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

def getskalajson(request):
    skalamikro      = UmkmModel.objects.filter(dtu_skalausha = 1)
    skalakecil      = UmkmModel.objects.filter(dtu_skalausha = 2)
    skalamenengah    = UmkmModel.objects.filter(dtu_skalausha = 3)

    context_data = {
        'sk_mikro'      : list(skalamikro.values()),
        'sk_kecil'      : list(skalakecil.values()),
        'sk_menengah'   : list(skalamenengah.values()),
    }

    return JsonResponse(context_data, safe= False)

def gethighomzet_umkm(request):
    high_omzukm     = UmkmModel.objects.all().order_by('-dtu_omzetthn')[:10]

    context_data = {
        'high_omzukm'      : list(high_omzukm.values()),
    }

    return JsonResponse(context_data, safe= False)

def gethighaset_umkm(request):
    high_astumkm      = UmkmModel.objects.all().order_by('-dtu_totalaset')[:10]

    context_data = {
        'high_astumkm'      : list(high_astumkm.values()),
    }

    return JsonResponse(context_data, safe= False)

def bidush_umkm(request):
    bdusahaumkm   = BidangUsaha.objects.all()
    umkmdata      = UmkmModel.objects.all()

    context_data = {
        'bidush_umkm'      : list(bdusahaumkm.values()),
        'umkm_data'      : list(umkmdata.values()),
    }

    return JsonResponse(context_data, safe= False)



def getallberita(request):
    list_berita = Article.objects.filter(ingallery = False).filter(ineducate = False)
    headline    =  Article.objects.filter(inheadline = True)


    all_series = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ingallery = False).filter(ineducate = False).order_by('-id')[:10]  

    paginator   = Paginator(list_berita, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    template = "berita/list_berita.html"
    list_data = {
        'sub_active'        : 'wartakumkm',
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
        'page_obj'          : page_obj,
        'headline'          : headline
    }
    return render (request, template, list_data)


def list_series(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).filter(ingallery = False).filter(ineducate = False)
    
    all_series    = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ingallery = False).filter(ineducate = False).order_by('-id')[:10]  


    paginator   = Paginator(matching_series, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    template = "berita/list_series.html"
    list_data = {
        # 'list_berita'       : list_berita,
        'sub_active'        : 'wartakumkm',
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
        'page_obj'          : page_obj,
    }
    return render (request, template, list_data)


def single_berita(request, series: str, article: str):
    matching_berita = Article.objects.filter(series__slug=series, article_slug=article).first()


    all_series = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ingallery = False).filter(ineducate = False).order_by('-id')[:10]  

    
    template = "berita/single_berita.html"
    list_data = {
        # 'list_berita'       : list_berita,
        'sub_active'        : 'wartakumkm',
        'berita'            : matching_berita,
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
    }
    return render (request, template, list_data)




def getallfakta(request):
    list_berita = Article.objects.filter(ineducate = True)
    headline    =  Article.objects.filter(inheadline = True).filter(ineducate = True)


    all_series = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ineducate = True).order_by('-id')[:10]  

    paginator   = Paginator(list_berita, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    template = "berita/list_fakta.html"
    list_data = {
        'sub_active'        : 'fakta',
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
        'page_obj'          : page_obj,
        'headline'          : headline
    }
    return render (request, template, list_data)


def list_series_fakta(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).filter(ineducate = True)
    
    all_series    = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ineducate = True).order_by('-id')[:10]  


    paginator   = Paginator(matching_series, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    template = "berita/list_series_fakta.html"
    list_data = {
        # 'list_berita'       : list_berita,
        'sub_active'        : 'fakta',
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
        'page_obj'          : page_obj,
    }
    return render (request, template, list_data)


def single_fakta(request, series: str, article: str):
    matching_berita = Article.objects.filter(series__slug=series, article_slug=article).first()


    all_series = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ineducate = True).order_by('-id')[:10]  

    
    template = "berita/single_fakta.html"
    list_data = {
        'sub_active'        : 'fakta',
        'berita'            : matching_berita,
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
    }
    return render (request, template, list_data)




def getallgallery(request):
    list_berita = Article.objects.filter(ingallery = True)
    headline    =  Article.objects.filter(inheadline = True).filter(ingallery = True)


    all_series = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ingallery = True).order_by('-id')[:10]  

    paginator   = Paginator(list_berita, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    template = "berita/list_gallery.html"
    list_data = {
        'sub_active'        : 'gallery',
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
        'page_obj'          : page_obj,
        'headline'          : headline
    }
    return render (request, template, list_data)


def list_series_gallery(request, series: str):
    matching_series = Article.objects.filter(series__slug=series).filter(ingallery = True)
    
    all_series    = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ingallery = True).order_by('-id')[:10]  


    paginator   = Paginator(matching_series, 6) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)
    
    template = "berita/list_series_gallery.html"
    list_data = {
        # 'list_berita'       : list_berita,
        'sub_active'        : 'gallery',
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
        'page_obj'          : page_obj,
    }
    return render (request, template, list_data)


def single_gallery(request, series: str, article: str):
    matching_berita = Article.objects.filter(series__slug=series, article_slug=article).first()


    all_series = ArticleSeries.objects.all()
    breaking_news = Article.objects.filter(ingallery = True).order_by('-id')[:10]  

    
    template = "berita/single_gallery.html"
    list_data = {
        'sub_active'        : 'gallery',
        'berita'            : matching_berita,
        'all_series'        : all_series,
        'breaking_news'     : breaking_news,
    }
    return render (request, template, list_data)


def front_regul_pdhk(request):
    searchfilter =""
    katefilter =""
    yearfilter =""
    
    tables_regulasi = RegulasiModel.objects.filter(type = 1)

    if request.GET:
        searchfilter = request.GET.get('searchfilter')
        katefilter = request.GET.get('katefilter')
        yearfilter = request.GET.get('yearfilter')
        query = (Q(title__icontains=searchfilter) & Q(kategori__icontains=katefilter) & Q(tahun__icontains=yearfilter)) 
        tables_regulasi = tables_regulasi.filter(query )


    paginator   = Paginator(tables_regulasi, 10)
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    list_data = {
        'sub_active'    : 'prodhk',
        'page_obj' : page_obj,
        'searchfilter':searchfilter,
        'katefilter':katefilter,
        'yearfilter':yearfilter,
    }
    
    return render (request, 'regul/front_regul_1.html', list_data)


def front_rapat_koor(request):
    searchfilter =""
    katefilter =""

    tables_regulasi = RegulasiModel.objects.filter(type = 2)

    if request.GET:
        searchfilter = request.GET.get('searchfilter')
        katefilter = request.GET.get('katefilter')
        query = (Q(title__icontains=searchfilter) & Q(kategori__icontains=katefilter) ) 
        tables_regulasi = tables_regulasi.filter(query )


    paginator   = Paginator(tables_regulasi, 10)
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    list_data = {
        'sub_active'    : 'rapatkoor',
        'page_obj' : page_obj,
        'searchfilter':searchfilter,
        'katefilter':katefilter,
    }
    
    return render (request, 'regul/front_regul_2.html', list_data)


def front_paparan(request):
    searchfilter =""

    tables_regulasi = RegulasiModel.objects.filter(type = 3)

    if request.GET:
        searchfilter = request.GET.get('searchfilter')
        query = (Q(title__icontains=searchfilter) ) 
        tables_regulasi = tables_regulasi.filter(query )


    paginator   = Paginator(tables_regulasi, 10)
    page_number = request.GET.get('page')
    page_obj    = paginator.get_page(page_number)

    list_data = {
        'sub_active'    : 'paparan',
        'page_obj' : page_obj,
        'searchfilter':searchfilter,
    }
    
    return render (request, 'regul/front_regul_3.html', list_data)


def contact_us(request):
    searchfilter =""
    if request.POST:
        form = FormSupportCenter(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            form = FormSupportCenter()
            messages.success(request, "Pesan berhasil terkirim")
            list_data = {
                'sub_active'    : 'contactus',
                'form'          : form,
            }

            return render(request, 'contact/cont_us.html', list_data)
        else:
            messages.error(request, "Pesan gagal terkirim")

    else:
        form = FormSupportCenter()

    list_data = {
        'sub_active'    : 'contactus',
        'form'          : form,
    }
    
    return render (request, 'contact/cont_us.html', list_data)

