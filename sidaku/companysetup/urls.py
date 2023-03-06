from django.urls import path
from . import views 

app_name = 'companysetup'

urlpatterns = [
	path('add', views.add_compsetup, name='newsetting'),
	path('update/<int:comp_id>', views.upd_compsetup, name='updsetting'),
	path('pesan_masuk', views.master_support, name='master_support'),
    path ('upmess', views.UpMessage, name='UpMessage'),
]