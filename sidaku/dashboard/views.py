from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.conf import settings

@login_required(login_url=settings.LOGIN_URL)
def dashboard(request):

    list_data = {
        'collapse_name' : '',
        'side_active'   : 'dash',
    }

    return render  (request, 'dashboard.html',list_data)