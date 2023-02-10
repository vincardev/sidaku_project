from django import template

register = template.Library()
from django.template.defaulttags import register


# @register.simple_tag
# def SplitVariableSosmed(stringval, type):
#     data = stringval.split(";")
#     retval=""
#     if (type == 0):
#        retval = data[0].split("#")[1]
#     elif (type == 1):
#        retval = data[1].split("#")[1]
    
#     return retval


@register.simple_tag
def GetjenisKoperasi(jenid):

    
    KSM     = 1
    SP      = 2
    JS      = 3
    PRD     = 4
    PMS     = 5

    JENIS_KOPERASI = [
        (KSM, ("Konsumen")),
        (SP, ("Simpan Pinjam")),
        (JS, ("Jasa")),
        (PRD, ("Produsen")),
        (PMS, ("Pemasaran"))
    ]

    value = ""
    for key,textstring in JENIS_KOPERASI:
        if key == jenid:
            value = textstring

    return value

@register.simple_tag
def GetListBulan(blnid):

    Jan     = 1
    Feb     = 2
    Mar     = 3
    Apr     = 4
    Mei     = 5
    Jun     = 6
    Jul     = 7
    Aug     = 8
    Sep     = 9
    Oct     = 10
    Nov     = 11
    Dec     = 12

    LIST_BULAN = [
        (Jan, ("Januari")),
        (Feb, ("Februari")),
        (Mar, ("Maret")),
        (Apr, ("April")),
        (Mei, ("Mei")),
        (Jun, ("Juni")),
        (Jul, ("Juli")),
        (Aug, ("Agustus")),
        (Sep, ("September")),
        (Oct, ("Oktober")),
        (Nov, ("November")),
        (Dec, ("Desember")),
    ]


    value = ""
    for key,textstring in LIST_BULAN:
        if key == blnid:
            value = textstring

    return value


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