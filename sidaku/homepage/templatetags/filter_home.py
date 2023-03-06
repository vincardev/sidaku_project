
from django.http import HttpResponseRedirect, Http404, FileResponse,HttpResponse
import io
from django import template
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4

from umkmdata.models import UmkmModel
from datetime import datetime, timedelta

register = template.Library()

@register.simple_tag
def pdf_view(path):
    with open(path, 'rb') as pdf:
        response = HttpResponse(pdf.read(), mimetype='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response
        pdf.closed

@register.simple_tag
def pdf_viewa(path):
    
    # try:
    return FileResponse(open(path, 'rb'), content_type='application/pdf')


@register.simple_tag
def getumkmskala(path):

    skalamikro      = UmkmModel.objects.filter(dtu_skalausha = 1)
    skalakecil      = UmkmModel.objects.filter(dtu_skalausha = 2)
    skalamenengah      = UmkmModel.objects.filter(dtu_skalausha = 3)
    
    # try:

    context_data = {
        'sk_mikro'      : skalamikro,
        'sk_kecil'      : skalakecil,
        'sk_menengah'   : skalamenengah,
    }
    return context_data

@register.simple_tag
def CheckUnreadDate(currentdate):

    ret_data = False
    if currentdate == datetime.now() - timedelta(days=90):
        ret_data = True
    
    return ret_data

@register.simple_tag
def CheckUnreadMessage(cdated, mdated):

    date_1 = cdated.strftime("%m/%d/%Y, %H:%M:%S")
    date_2 = mdated.strftime("%m/%d/%Y, %H:%M:%S")

    res_data= False
    if date_1 ==  date_2:
        res_data = True
    return res_data


# from camppackages.models import PackagesItemsDetail
# 
# from django.template.defaulttags import register


# @register.simple_tag
# def SplitVariableSosmed(stringval, type):
#     data = stringval.split(";")
#     retval=""
#     if (type == 0):
#        retval = data[0].split("#")[1]
#     elif (type == 1):
#        retval = data[1].split("#")[1]
    
#     return retval


# @register.simple_tag
# def GetPackagesItemsDetail(packid):
#     value = PackagesItemsDetail.objects.filter(dpiPackID = packid )
#     return value


# @register.simple_tag
# def GetRoomsRatesNormal(roomid):
#     value = RoomRates.objects.get(rateRoomID = roomid, rateIsSpecific = False )
#     return value

# @register.simple_tag
# def AdSubRates(old, qty, rates):
#     old = old + (qty * rates)
#     return old

# @register.simple_tag
# def GetCountKelurahan(idbri):
#     detail = DetailAreaBRiUnit.objects.filter(idbri = idbri)
#     return detail

# def GetListKelurahan(value, idbri):
#     value = DetailAreaBRiUnit.objects.filter(idbri = idbri)
#     return value

# register.filter('GetListKelurahan', GetListKelurahan)


# def GetListMantri(value, idbri):
#     value = DetailAreaBRiUnit.objects.filter(idbri = idbri).values('idmantri').distinct()
#     return value
    
# register.filter('GetListMantri', GetListMantri)



# # @register.tag(name='GetListMitra')
# @register.simple_tag
# def GetListMitra(idbri):
#     detail = DetailMitraBRIUnit.objects.filter(idbri = idbri)
#     return detail

# @register.simple_tag
# def GetListWilayah(idbri):
#     detail = DetailAreaBRiUnit.objects.filter(idbri = idbri)
#     return detail
    

# def tambah(value, args):
#     value = value + args
#     return value


# register.filter('tambah', tambah)