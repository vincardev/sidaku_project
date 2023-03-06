from django.urls import path
from . import views

app_name = 'umkmdata'

urlpatterns = [

	path('master', views.master_umkm, name='master_umkm'),
	path('add', views.add_umkm, name='add_umkm'),
	path('delete/<int:umkm_id>', views.del_umkm, name='del_umkm'),
	path('update/<int:umkm_id>', views.upd_umkm, name='upd_umkm'),
	
    path ('tabledata/<int:umkm_id>', views.getjsontable, name='jsontabledata'),
    path ('proddata/<int:prod_id>', views.getjsonproduk, name='jsonprodukdata'),

]