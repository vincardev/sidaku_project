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
def GetKategoriName(typeid):

    UU     = 1
    PUU    = 2
    PPEM   = 3
    PPRES  = 4
    KIP    = 5
    PMEN   = 6
    KEPMEN = 7
    KEPDEP = 8
    PTER   = 9
    PETPEL = 10
    SUED   = 11

    KATEGORI_CHOICES = [
        (UU, ("Undang-Undang")),
        (PUU, ("Perancangan Undang-Undang")),
        (PPEM, ("Peraturan Pemerintah")),
        (PPRES, ("Peraturan Presiden")),
        (KIP, ("Keputusan dan Intruksi Presiden")),
        (PMEN, ("Peraturan Mentri")),
        (KEPMEN, ("Keputusan Mentri")),
        (KEPDEP, ("Keputusan Deputi")),
        (PTER, ("Peraturan Terkait")),
        (PETPEL, ("Petunjuk Pelaksanaan")),
        (SUED, ("Surat Edaran")),
    ]


    value = ""
    for key,textstring in KATEGORI_CHOICES:
        if key == typeid:
            value = textstring
            
    # value = KATEGORI_CHOICES[typeid][1]

    return value

@register.simple_tag
def GetListKategori():

    UU     = 1
    PUU    = 2
    PPEM   = 3
    PPRES  = 4
    KIP    = 5
    PMEN   = 6
    KEPMEN = 7
    KEPDEP = 8
    PTER   = 9
    PETPEL = 10
    SUED   = 11

    KATEGORI_CHOICES = [
        (UU, ("Undang-Undang")),
        (PUU, ("Perancangan Undang-Undang")),
        (PPEM, ("Peraturan Pemerintah")),
        (PPRES, ("Peraturan Presiden")),
        (KIP, ("Keputusan dan Intruksi Presiden")),
        (PMEN, ("Peraturan Mentri")),
        (KEPMEN, ("Keputusan Mentri")),
        (KEPDEP, ("Keputusan Deputi")),
        (PTER, ("Peraturan Terkait")),
        (PETPEL, ("Petunjuk Pelaksanaan")),
        (SUED, ("Surat Edaran")),
    ]
    
    return KATEGORI_CHOICES



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