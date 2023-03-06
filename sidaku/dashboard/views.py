from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings
from koperasi.models import KoperasiModel
from companysetup.models import SupportCenterModel
from umkmdata.models import UmkmModel
from userprofile.models import UserProfile
from datetime import datetime, timedelta

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):
    dataumkm = UmkmModel.objects.all()
    datakoperasi = KoperasiModel.objects.all()
    dataUser = UserProfile.objects.all()
    Inbox = SupportCenterModel.objects.all()

    unread = 0
    for sc in Inbox:
        if (sc.created_date.strftime("%m/%d/%Y, %H:%M:%S") == sc.modified_date.strftime("%m/%d/%Y, %H:%M:%S")):
            unread += 1


    list_data = {
        'collapse_name' : '',
        'side_active'   : 'dash',
        'umkmdata'   : dataumkm,
        'kopdata'   : datakoperasi,
        'userdata'   : dataUser,
        'unread'   : unread,
        'pesanmasuk'   : Inbox,
    }

    return render  (request, 'dashboard.html',list_data)