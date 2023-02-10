from django import template

register = template.Library()
from django.template.defaulttags import register

@register.simple_tag
def GetBentukUsaha(id):
    PERO    = 1
    CV      = 2
    UD      = 3
    KOP     = 4
    DLL     = 5

    BENTUK_USAHA = [
        (PERO, ("Perorangan")),
        (CV, ("CV")),
        (UD, ("UD")),
        (KOP, ("Koperasi")),
        (DLL, ("Lainnya"))
    ]

    value = ""
    for key,textstring in BENTUK_USAHA:
        if key == id:
            value = textstring

    return value

@register.simple_tag
def GetBidangUsaha(id):
    MADK    = 1
    MIDK    = 2
    KRJ     = 3
    PDG     = 4
    JS      = 5
    LL      = 6

    BIDANG_USAHA = [
        (MADK, ("Makanan dalam Kemasan")),
        (MIDK, ("Minuman dalam Kemasan")),
        (KRJ, ("Kerajinan")),
        (PDG, ("Perdagangan")),
        (JS, ("Jasa")),
        (LL, ("Lainnya")),
    ]

    value = ""
    for key,textstring in BIDANG_USAHA:
        if key == id:
            value = textstring

    return value

@register.simple_tag
def GetSkalaUsaha(id):
   
    MKR    = 1
    KCL    = 2
    MNG    = 3

    SKALA_USAHA = [
        (MKR, ("Mikro")),
        (KCL, ("Kecil")),
        (MNG, ("Menengah"))
    ]

    value = ""
    for key,textstring in SKALA_USAHA:
        if key == id:
            value = textstring

    return value

