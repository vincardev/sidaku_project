from django.urls import path
from . import views

app_name = 'keuangan'

urlpatterns = [

	path('master', views.master_keu, name='master_keu'),
	path('add', views.add_keu, name='add_keu'),
	path('update/<int:keu_id>', views.upd_keu, name='upd_keu'),
	path('delete/<int:keu_id>', views.del_keu, name='del_keu'),

	path('add_umkm', views.add_keu_umkm, name='add_keu_umkm'),
	path('update_umkm/<int:keu_id>', views.upd_keu_umkm, name='upd_keu_umkm'),
	path('delete_umkm/<int:keu_id>', views.del_keu_umkm, name='del_keu_umkm'),
	
    # path ('getprodkop/<int:kop_id>', views.getjsonprodkop, name='prodkop'),

]