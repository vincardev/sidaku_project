
from django.http import HttpResponseRedirect, Http404, FileResponse,HttpResponse
import io
from django import template
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.pagesizes import A4

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
    # except FileNotFoundError:
    #     raise Http404() 


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